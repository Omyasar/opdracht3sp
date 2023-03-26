import psycopg2
import random

psql_conn = psycopg2.connect(
    host="localhost",
    database="document_store",
    user="postgres",
    password="farmainterim",
    port=5433)

psql_cursor = psql_conn.cursor()


# Maak tables aan voor de content filtered recommendation en collab filtered recommendations.
# psql_cursor.execute("CREATE TABLE content_filtered_recommendations (recommendation_id SERIAL PRIMARY KEY, product_id INTEGER, sub_category VARCHAR, doelgroep VARCHAR);")
# psql_cursor.execute("CREATE TABLE collab_filtered_recommendations (recommendation_id SERIAL PRIMARY KEY, product_id INTEGER, user_id INTEGER);")

# Content filtering aanbeveling op basis van doelgroep en soort.
def content_filtered():
    psql_cursor.execute("SELECT DISTINCT soort, doelgroep FROM products;")
    subcategory_en_doelgroep = psql_cursor.fetchall()

    for soort, doelgroep in subcategory_en_doelgroep:
        producten = get_products(soort, doelgroep)
        for product in producten:
            psql_cursor.execute(
                "INSERT INTO content_filtered_recommendations (product_id, soort, doelgroep) VALUES (%s, %s, %s);",
                (product[0], soort, doelgroep))


# Met deze functie pakken we met een query de soort en doelgroep van een gegeven soort en doelgroep.
def get_products(soort, doelgroep):
    psql_cursor.execute(
        "SELECT product_id, soort, price, name, doelgroep FROM products WHERE soort = %s AND doelgroep = %s;",
        (soort, doelgroep))
    result = psql_cursor.fetchall()
    return result


def random_sample_products(product_list, sample_size):
    return random.sample(product_list, sample_size)


soort = 'Accu en batterijen'
doelgroep = 'Volwassenen'
num_samples = 5

products = get_products(soort, doelgroep)
random_products = random_sample_products(products, num_samples)
