import sqlite3
sqliteConnection=sqlite3.connect("Bank.db")
cursor=sqliteConnection.cursor()
cursor.close()
sqliteConnection.close()
"==========================================================="
import sqlite3
sqliteConnection=sqlite3.connect("Bank.db")
cursor=sqliteConnection.cursor()
sqlite_create_table_query='''CREATE TABLE Details(
                             Name TEXT NOT NULL,
                             AccountNum INTEGER PRIMARY KEY,
                             Balance INTEGER NOT NULL,
                             UniqueNum INTEGER UNIQUE);'''
cursor.execute(sqlite_create_table_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()
"=========================================================="
import sqlite3
sqliteConnection=sqlite3.connect("Bank.db")
cursor=sqliteConnection.cursor()
sqlite_create_table_query='''CREATE TABLE CreateAccount(
                             Name TEXT NOT NULL,
                             PassportNum INTEGER PRIMARY KEY,
                             PhysicalAddress TEXT NOT NULL,
                             PhoneNum INTEGER UNIQUE,
                             AccountNum INTEGER UNIQUE);'''
cursor.execute(sqlite_create_table_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()
'''======================================================='''
import sqlite3
sqliteConnection=sqlite3.connect("Bank.db")
cursor=sqliteConnection.cursor()
sqlite_create_table_query='''CREATE TABLE Deposits(
                             Name TEXT NOT NULL,
                             PassportNum INTEGER PRIMARY KEY,
                             AccountNum INTEGER UNIQUE,
                             Amount INTEGER NOT NULL,
                             Date INTEGER NOT NULL);'''
cursor.execute(sqlite_create_table_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()
'''======================================================'''
import sqlite3
sqliteConnection=sqlite3.connect("Bank.db")
cursor=sqliteConnection.cursor()
sqlite_create_table_query='''CREATE TABLE Withdrawals(
                             Name TEXT NOT NULL,
                             PassportNum INTEGER PRIMARY KEY,
                             AccountNum INTEGER UNIQUE,
                             Amount INTEGER NOT NULL,
                             Charges INTEGER NOT NULL,
                             Date INTEGER NOT NULL);'''
cursor.execute(sqlite_create_table_query)
sqliteConnection.commit() 
cursor.close()
sqliteConnection.close()
'''========================================================'''
import sqlite3
sqliteConnection=sqlite3.connect("Bank.db")
cursor=sqliteConnection.cursor()
sqlite_create_table_query='''CREATE TABLE Loan(
                             Name TEXT NOT NULL,
                             PassportNum INTEGER PRIMARY KEY,
                             AccountNum INTEGER UNIQUE,
                             Type TEXT NOT NULL,
                             Amount INTEGER NOT NULL,
                             InterestType TEXT NOT NULL,
                             TotalPayAtEnd INTGER NOT NULL,
                             Date INTEGER NOT NULL);'''
cursor.execute(sqlite_create_table_query)
sqliteConnection.commit() 
cursor.close()
sqliteConnection.close()
