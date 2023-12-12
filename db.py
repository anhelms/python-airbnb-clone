import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS rooms;
        """
    )
    conn.execute(
        """
        CREATE TABLE rooms (
          id INTEGER PRIMARY KEY NOT NULL,
          name STRING,
          city STRING,
          state STRING
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    rooms_seed_data = [
        ("1st room", "Los Angeles", "CA"),
        ("2nd room", "Los Angeles", "CA"),
        ("3rd room", "Los Angeles", "CA"),
    ]
    conn.executemany(
        """
        INSERT INTO rooms (name, city, state)
        VALUES (?,?,?)
        """,
        rooms_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()


def rooms_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM rooms
        """
    ).fetchall()
    return [dict(row) for row in rows]


def rooms_create(name, city, state):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO rooms (name, city, state)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (name, city, state),
    ).fetchone()
    conn.commit()
    return dict(row)


def rooms_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM rooms
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)


def rooms_update_by_id(id, name, city, state):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE rooms SET name = ?, city = ?, state = ?
        WHERE id = ?
        RETURNING *
        """,
        (name, city, state, id),
    ).fetchone()
    conn.commit()
    return dict(row)


def rooms_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from rooms
        WHERE id = ?
        """,
        id,
    )
    conn.commit()
    return {"message": "Room destroyed successfully"}