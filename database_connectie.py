import psycopg2

def database_connectie():
    psql_conn = psycopg2.connect(
        host="localhost",
        database="document_store",
        user="postgres",
        password="farmainterim",
        port=5433)

    psql_cursor = psql_conn.cursor()
    return psql_conn, psql_cursor