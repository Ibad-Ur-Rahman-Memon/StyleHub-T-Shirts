# test_db.py
import mysql.connector


def test_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="stylehub_tshirts"
        )
        cursor = conn.cursor()

        # Test 1: Check if table exists
        cursor.execute("SHOW TABLES LIKE 't_shirts'")
        print("Table exists:", cursor.fetchone() is not None)

        # Test 2: Count records
        cursor.execute("SELECT COUNT(*) FROM t_shirts")
        print("Total t-shirts:", cursor.fetchone()[0])

        # Test 3: Sample query
        cursor.execute("SELECT brand, color, size FROM t_shirts LIMIT 5")
        print("\nSample records:")
        for row in cursor:
            print(row)

    except Exception as e:
        print("Error:", e)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


test_connection()