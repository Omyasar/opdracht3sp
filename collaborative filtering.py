from database_connectie import database_connectie

# Verbinding maken met de database via de database_connectie module
psql_conn, psql_cursor = database_connectie()


# recommendations_id = '222' is eigelijk een profiel ID
# Functie om eerder aanbevolen producten op te halen op basis van het recommendations_id (eigenlijk een profiel ID).
def previously_recommended_id_query():
    psql_cursor.execute("select previously_recommended from recommendations where recommendations_id = '222'")
    result = psql_cursor.fetchall()
    previously_recommended = [int(id) for id in result[0][0].strip('{}').split(',')]
    return previously_recommended


# Haal de eerder aanbevolen producten op.
previously_recommended_id_query()


# query kenmerken data
# Functie om kenmerken op te halen voor een lijst van producten.
def kenmerken_product_ids(kenmerken_list):
    psql_cursor.execute("SELECT soort, gender FROM products WHERE product_id IN ({})".format(
        ",".join(str(int(id)) for id in kenmerken_list)))
    result = psql_cursor.fetchall()
    soort_value = []
    gender_value = []

    for row in result:
        soort_value.append(row[0])
        gender_value.append(row[1])
    return soort_value, gender_value


# Haal de kenmerken op voor de eerder aanbevolen producten.
kenmerken_product_ids(kenmerken_list=previously_recommended_id_query())
soort_value, gender_value = kenmerken_product_ids(kenmerken_list=previously_recommended_id_query())
soort_value = (soort_value[0])
gender_value = (gender_value[0])


# Functie om producten op te halen op basis van soort en gender.
def soort_gender_query(gender_value, soort_value):
    psql_cursor.execute(
        "select product_id from products where soort = %s AND gender = %s ORDER BY BRAND ASC limit 4",
        (soort_value, gender_value))
    result = psql_cursor.fetchall()
    soort_gender_list = []
    for row in result:
        soort_gender_list.append(row)
    return soort_gender_list


categorie_doelgroep_ids = soort_gender_query(gender_value, soort_value)


# Functie om de aanbevolen producten op te slaan in de database.
def insert_collab(categorie_doelgroep_ids):
    psql_cursor.execute("delete from collab_filtered_products")
    for id_tuple in categorie_doelgroep_ids:
        psql_cursor.execute("INSERT INTO collab_filtered_products (product_id) VALUES (%s)", id_tuple)
    psql_conn.commit()


# Sla de aanbevolen producten op in de database.

insert_collab(categorie_doelgroep_ids)
