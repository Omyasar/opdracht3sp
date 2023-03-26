from database_connectie import database_connectie

# Verbinding maken met de database via de database_connectie module
psql_conn, psql_cursor = database_connectie()


# Functie om categorie en geslacht op te halen op basis van het product_id
def kenmerken_prod_id(kenmerk):
    psql_cursor.execute("SELECT categorie, gender FROM products WHERE product_id = %s",
                        kenmerk)
    result = psql_cursor.fetchall()
    categorie_value = []
    gender_value = []
    for row in result:
        categorie_value.append(row[0])
        gender_value.append(row[1])
    return gender_value, categorie_value


# Functie om product_ids op te halen die overeenkomen met de gegeven categorie en geslacht waarden
def gender_category_ids(gender_value, categorie_value):
    psql_cursor.execute(
        "SELECT product_id FROM products WHERE gender = ANY(%s) AND categorie = ANY(%s) ORDER BY price DESC LIMIT 4",
        (gender_value, categorie_value))
    result = psql_cursor.fetchall()
    gender_category_list = []
    for row in result:
        gender_category_list.append(row)
    return gender_category_list


# Test variabele
test_id = (2043,)

# Haal categorie en geslacht op basis van het test_id
gender_value, categorie_value = kenmerken_prod_id(kenmerk=test_id)

# Haal product_ids op die overeenkomen met de opgehaalde categorie en geslacht.
gender_category_list = gender_category_ids(gender_value, categorie_value)
print(gender_category_list)


# Functie om aanbevolen producten in de database te wissen en in te voegen
def insert_content(content_ids):
    psql_cursor.execute("delete from content_filtered_recommendations")
    for id_content in content_ids:
        psql_cursor.execute("INSERT INTO content_filtered_recommendations (product_id) VALUES (%s)", id_content)
    psql_conn.commit()


# Voeg de opgehaalde product_ids toe aan de aanbevolen producten in de database
insert_content(content_ids=gender_category_list)
