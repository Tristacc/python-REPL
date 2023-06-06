
import sqlite3
import os
from transaction import Transaction


transaction = Transaction()
sample_item = {
    'item_num': 1,
    'amount': 50,
    'category': 'Groceries',
    'date': '0205',
    'description': 'Bread and milk'
}

# prepare -- delect all
def clearTable():
    con= sqlite3.connect(os.getenv('HOME')+'/Desktop/my-repo/python-practice/PA03/transactions.db')
    cur = con.cursor() 
    cur.execute("DELETE FROM transactions")
    con.commit()
    con.close()

# get number of data in the table
def num_data():
    con= sqlite3.connect(os.getenv('HOME')+'/Desktop/my-repo/python-practice/PA03/transactions.db')
    cur = con.cursor() 
    cur.execute("SELECT COUNT(*) FROM transactions")
    count = cur.fetchone()[0]
    con.close()
    return count

def test_add():
    clearTable()
    #add one data
    transaction.add(sample_item)
    count =  num_data()
    assert count == 1

def test_delete():
    userInput = {'item_num':1}
    transaction.delete(userInput)
    count =  num_data()
    assert count == 0
