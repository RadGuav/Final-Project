def check_for_updates(conn, table, previous_instance):
    """takes a time as previous instance
        queries the database for updates since that time
        if resulting rows are greater than 0 then it will return true
    """

    cursor = conn.cursor()
    print(f"SELECT * FROM {table} WHERE last_updated > '{previous_instance}';")
    cursor.execute(f"SELECT * FROM {table} WHERE last_updated > '{previous_instance}';")
    rows = cursor.fetchall()

    if len(rows) > 0: 
        return True
    