
import os
import sys

import sqlite3
from sqlite3 import Error
from flask import Flask
from flask import request
from flask import render_template
from tkinter import messagebox
import exbody
import calfunction




app = Flask(__name__)

def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

@app.route('/output')
def my_form_output():
    database = "C:\\sqlite\\db\\finance.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM calfinance WHERE inoutflag=? ORDER BY id ASC", (2,))

        rows = cur.fetchall()
        outarr = []
        for row in rows:
            outarr.append(str(row[2]))
            #print(row)
        straaa = outarr[0]
        strbbb= outarr[1]
        strccc = outarr[2]
    return render_template("output.html", useraaa=straaa, userbbb=strbbb, userccc= strccc)  # this should be the name of your html file



@app.route('/')
def my_form():
    return render_template("hello.html") # this should be the name of your html file


@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."

    fvalue1 = request.form['text1']
    fvalue2 = request.form['text2']
    fvalue3 = request.form['text3']
    fvalue4 = request.form['text4']
    fvalue5 = request.form['text5']

    fin1 = float(fvalue1)
    fin2 = float(fvalue2)
    fin3 = float(fvalue3)
    fin4 = float(fvalue4)
    fin5 = float(fvalue5)

    exbody.main(fin1, 'input1')
    exbody.main(fin2, 'input2')
    exbody.main(fin3, 'input3')
    exbody.main(fin4, 'input4')
    exbody.main(fin5, 'input5')
    calfunction.main()

    database = "C:\\sqlite\\db\\finance.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM calfinance WHERE inoutflag=? ORDER BY id ASC", (2,))

        rows = cur.fetchall()
        outarr = []
        for row in rows:
            outarr.append(str(row[2]))
            # print(row)
        straaa = outarr[0]
        strbbb = outarr[1]
        strccc = outarr[2]
    return render_template("output.html", useraaa=straaa, userbbb=strbbb, userccc=strccc)



@app.route('/', methods=['POST'])
def my_form_post():

    fvalue1 = request.form['text1']
    fvalue2 = request.form['text2']
    fvalue3 = request.form['text3']
    fvalue4 = request.form['text4']
    fvalue5 = request.form['text5']

    fin1 = float(fvalue1)
    fin2 = float(fvalue2)
    fin3 = float(fvalue3)
    fin4 = float(fvalue4)
    fin5 = float(fvalue5)

    exbody.main(fin1,'input1')
    exbody.main(fin2,'input2')
    exbody.main(fin3,'input3')
    exbody.main(fin4,'input4')
    exbody.main(fin5,'input5')
    calfunction.main()
    return my_form_output()





if __name__ == '__main__':
    app.run(debug=True)


