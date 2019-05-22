import sqlite3
from sqlite3 import Error
import array as arr

import upgrade


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


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM calfinance ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row[5])
        # print(row)


def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE calfinance
              SET fvalue = ? 
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, task)


def select_task_by_priority():

    database = "C:\\sqlite\\db\\finance.db"
     # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Get all database array:")
        curall = conn.cursor()
        curall.execute("SELECT * FROM calfinance ORDER BY id ASC")
        rowsall = curall.fetchall()
        totaldata = []
        for row1 in rowsall:
            totaldata.append(row1)
    conn.close()

    conn = create_connection(database)
    logicarr = []
    with conn:
        print("2. Get Mathlogic +-part:")
        cur = conn.cursor()
        cur.execute("SELECT * FROM calfinance WHERE mathflag=? ORDER BY id ASC", (1,))
        rows = cur.fetchall()

        for row in rows:
            logicarr.append(row)
    conn.close()

    for tempVar in logicarr:
        alltxt = tempVar[4]
        a=0
        b=0
        c=0
        d=0
        if alltxt[2:3] == "+":
                splitp = alltxt.split("+")
                a = int(splitp[0])
                b = totaldata[a - 1][2]
                c = int(splitp[1])
                d = totaldata[c - 1][2]
                sum = float(b) + float(d)
                upgrade.main(sum, tempVar[0])
                print(a, b, c, d, sum)

                database = "C:\\sqlite\\db\\finance.db"
                # create a database connection
                conn = create_connection(database)
                with conn:
                    print("1. Get all database array:")
                    curall = conn.cursor()
                    curall.execute("SELECT * FROM calfinance ORDER BY id ASC")
                    rowsall = curall.fetchall()
                    totaldata = []
                    for row1 in rowsall:
                        totaldata.append(row1)
                conn.close()

        elif alltxt[2:3] == "-":
                splitp = alltxt.split("-")
                a = int(splitp[0])
                b = totaldata[a - 1][2]
                c = int(splitp[1])
                d = totaldata[c - 1][2]
                sum = float(b) - float(d)
                upgrade.main(sum, tempVar[0])
                print(a, b, c, d, sum)

                database = "C:\\sqlite\\db\\finance.db"
                # create a database connection
                conn = create_connection(database)
                with conn:
                    print("1. Get all database array:")
                    curall = conn.cursor()
                    curall.execute("SELECT * FROM calfinance ORDER BY id ASC")
                    rowsall = curall.fetchall()
                    totaldata = []
                    for row1 in rowsall:
                        totaldata.append(row1)
                conn.close()

        else:
                print(1)

    conn = create_connection(database)
    logicarrier = []
    with conn:
        print("2. Get Mathlogic +-part:")
        cur = conn.cursor()
        cur.execute("SELECT * FROM calfinance WHERE mathflag=? ORDER BY id ASC", (3,))
        rows = cur.fetchall()

        for row in rows:
            logicarrier.append(row)
    conn.close()

    for tempVar1 in logicarrier:
        alltxt = tempVar1[4]
        a=0
        b=0
        c=0
        d=0
        if alltxt[2:3] == "/":
                splitp = alltxt.split("/")
                a = int(splitp[0])
                b = totaldata[a - 1][2]
                c = int(splitp[1])
                d = totaldata[c - 1][2]
                sum = float(b) / float(d)
                upgrade.main(sum, tempVar1[0])
                print(a, b, c, d, sum)

                database = "C:\\sqlite\\db\\finance.db"
                # create a database connection
                conn = create_connection(database)
                with conn:
                    print("1. Get all database array:")
                    curall = conn.cursor()
                    curall.execute("SELECT * FROM calfinance ORDER BY id ASC")
                    rowsall = curall.fetchall()
                    totaldata = []
                    for row1 in rowsall:
                        totaldata.append(row1)
                conn.close()

        elif alltxt[2:3] == "*":
                splitp = alltxt.split("*")
                a = int(splitp[0])
                b = totaldata[a - 1][2]
                c = int(splitp[1])
                d = totaldata[c - 1][2]
                sum = float(b) * float(d)
                upgrade.main(sum, tempVar1[0])
                print(a, b, c, d, sum)

                database = "C:\\sqlite\\db\\finance.db"
                # create a database connection
                conn = create_connection(database)
                with conn:
                    print("1. Get all database array:")
                    curall = conn.cursor()
                    curall.execute("SELECT * FROM calfinance ORDER BY id ASC")
                    rowsall = curall.fetchall()
                    totaldata = []
                    for row1 in rowsall:
                        totaldata.append(row1)
                conn.close()

        else:
                print(1)

def main():

        select_task_by_priority()


if __name__ == '__main__':
    main()