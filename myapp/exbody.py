import sqlite3
from sqlite3 import Error


def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE calfinance
              SET fvalue = ? 
              WHERE dataflag = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def main(fvalue,finput):
    database = "C:\\sqlite\\db\\finance.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_task(conn, (fvalue, str(finput)))


if __name__ == '__main__':
    main()

