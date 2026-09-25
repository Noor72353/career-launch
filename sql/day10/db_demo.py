import sqlite3

import pandas as pd

DB_NAME = "practice.db"


def main():
    """Run the SQLite database demonstration."""
    connection = None

    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        print("Database connection successful.")

        # INSERT
        cursor.execute(
            """
            INSERT INTO users (name, email, city)
            VALUES (?, ?, ?)
            """,
            ("Python User", "python@example.com", "Islamabad"),
        )

        connection.commit()
        print("User inserted successfully.")

        # UPDATE
        cursor.execute(
            """
            UPDATE users
            SET city = ?
            WHERE email = ?
            """,
            ("Rawalpindi", "python@example.com"),
        )

        connection.commit()
        print("User updated successfully.")

        # DELETE
        cursor.execute(
            """
            DELETE FROM users
            WHERE email = ?
            """,
            ("python@example.com",),
        )

        connection.commit()
        print("User deleted successfully.")

        # Parameterized SELECT
        cursor.execute(
            """
            SELECT id, name, email, city
            FROM users
            WHERE city = ?
            """,
            ("Islamabad",),
        )

        users = cursor.fetchall()

        print("Users in Islamabad:")
        for user in users:
            print(user)

        # Pandas integration
        users_df = pd.read_sql_query(
            """
            SELECT id, name, email, city
            FROM users
            """,
            connection,
        )

        print("Users DataFrame:")
        print(users_df)

    except sqlite3.Error as error:
        print(f"Database error: {error}")

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    main()
