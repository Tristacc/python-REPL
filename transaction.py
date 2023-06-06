
# this file handle the logic of inserting data to db
import sqlite3
import os

# query --> dic for checking
def toDict(t):
    transaction = {'rowid':t[0], 'item_num':t[1], 'amount':t[2], 'category':t[3], 'date':t[4],'description':t[5]}
    return transaction

class Transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num int, amount int, category text, date text, description text)''',())
    # ''' create a transaction and add it to the transactions table '''    
    def add(self, item):
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_num'],item['amount'],item['category'],item['date'],item['description']))
     # return all the data from the table
    def showTransactions(self):
        return self.runQuery("SELECT rowid,* from transactions",())
    
    def delete(self, item):
        return self.runQuery("DELETE FROM transactions WHERE item_num=(?)",(item['item_num'],))

    def sumByDate(self):
        return self.runQuery("SELECT date AS col1, * FROM transactions group by date",())
    

    #上面的function 會把query的指令傳進來 由runQuery對database做執行
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/Desktop/my-repo/python-practice/python-REPL/transactions.db')
        cur = con.cursor() 
        '''run上面的query'''
        cur.execute(query,tuple)
        '''fetches all rows returned by the executed query and stores them in the tuples variable.'''
        tuples = cur.fetchall()
        '''#db 修改檔案必做 .commit() == .save()'''
        con.commit()
        con.close()
        '''把結果存在dic for checking'''
      
        return [toDict(t) for t in tuples]