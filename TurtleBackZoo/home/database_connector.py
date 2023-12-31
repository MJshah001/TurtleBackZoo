import psycopg2
from contextlib import closing
from django.conf import settings

def get_connection():
    return psycopg2.connect(
    dbname="TurtleBackZoo",
    user="postgres",
    password="root1234",
    host="localhost",
    port="5432"
    )

def execute_query(query, *args, query_type="SELECT"):
    with closing(get_connection()) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            if query_type == "SELECT":
                return cursor.fetchall(), True  # Return rows and success flag
            elif query_type == "INSERT":
                conn.commit()
                # Optionally return the last inserted ID
                return cursor.fetchone()[0], True  # Return inserted ID and success flag
            elif query_type == "UPDATE" or query_type == "DELETE":
                rows_affected = cursor.rowcount  # Get the number of rows affected
                conn.commit()
                if rows_affected > 0:
                    return rows_affected, True  # Return number of rows affected and success flag
                else:
                    return 0, False  # Return failure flag if no rows were affected

