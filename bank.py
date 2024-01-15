import sqlite3
sqliteConnection=sqlite3.connect("Bank.db")
sqliteConnection.row_factory = lambda cursor, row: row[0]
cursor=sqliteConnection.cursor()
name=cursor.execute("SELECT Name from Details").fetchall()
names=[]
for val in name:
    names.append(val)
accountnum=cursor.execute("SELECT AccountNum from Details").fetchall()
accountnums=[]
for val in accountnum:
    accountnums.append(val)
balance=cursor.execute("SELECT Balance from Details").fetchall()
balances=[]
for val in balance:
    balances.append(val)

class bank:
    def __init__(self, name):
        self.name=name
    def checkdetails(self):
        x=int(input("Enter your account number:"))
        if x in accountnums:
            i=accountnums.index(x)
            details={"Name":[names[i]],
                     "Account Number":[accountnums[i]],
                     "Balance":[balances[i]]}
            import pandas as pd
            brics=pd.DataFrame(details)
            print(brics)
        else:
            print("Invalid Input") 
    def createaccount(self):
        a=input("Enter your name:")
        b=int(input("Enter your passport number:"))
        c=input("Enter your physical address:")
        d=int(input("Enter your phone number:"))
        e=accountnums[-1]+132
        f=int(input("Enter the amount you would like to deposit in your new bank account-> this is a compulsary process, bank account cannot be empty."))
        param=(a,b,c,d,e,f)
        params=(a,e,f)
        import sqlite3
        sqliteConnection=sqlite3.connect("Bank.db")
        cursor=sqliteConnection.cursor()
        cursor.execute("INSERT INTO CreateAccount(Name, PassportNum, PhysicalAddress, PhoneNum, AccountNum, Amount) VALUES(?, ?, ?, ?, ?, ?)", param)
        cursor.execute("INSERT INTO Details(Name, AccountNum, Balance) VALUES(?, ?, ?)", params)
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection.close()
        print("New Bank Account Created")
    def deposits(self):
        c=int(input("Enter your account number:"))
        i=accountnums.index(c)
        a=names[i]
        if a in names and c in accountnums:
            d=int(input("Enter the amount you wish to deposit into your bank account:"))
            e=input("Enter the date:")
            param=(a,c,d,e)
            i=names.index(a)
            f=balances[i]+d
            import sqlite3
            sqliteConnection=sqlite3.connect("Bank.db")
            cursor=sqliteConnection.cursor()
            cursor.execute("INSERT INTO Deposits(Name, AccountNum, Amount, Date) VALUES(?, ?, ?, ?)", param)
            sql_update_query="""Update Details set Balance = ? where AccountNum=?"""
            data=(f,c)
            cursor.execute(sql_update_query, data) 
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()
            print("Your new balance->",f)
        else:
            print("Invalid Input")
    def withdrawals(self):
        c=int(input("Enter your account number:"))
        i=accountnums.index(c)
        a=names[i]
        if c in accountnums:
            d=int(input("Enter the amount you wish to withdraw from your bank account:"))
            if d>balances[i]:
                print("Sorry, request not processed, not enough balance.")
            else:
                e=input("Enter the date:")
                param=(a,c,d,e)
                i=names.index(a)
                f=balances[i]-d
                import sqlite3
                sqliteConnection=sqlite3.connect("Bank.db")
                cursor=sqliteConnection.cursor()
                cursor.execute("INSERT INTO Withdrawals(Name, AccountNum, Amount, Date) VALUES(?, ?, ?, ?)", param)
                sql_update_query="""Update Details set Balance = ? where AccountNum=?"""
                data=(f,c)
                cursor.execute(sql_update_query, data)
                sqliteConnection.commit()
                cursor.close()
                sqliteConnection.close()
                print("Your new balance->",f)
        else:
            print("Invalid Input")
    def loans(self):
        c=input("Enter your name:")
        d=int(input("Enter your passport number:"))
        e=int(input("Enter your account number:"))
        a=int(input("Enter the type of loan you wish to process, 1 for long-term loans and 2 for short-term loans:"))
        f=int(input("Enter the number of years you wish to keep the loan for:"))
        g=float(input("Enter the amount:"))
        j=input("Enter the date:")
        if a==1:
            b="Compound Interest"
            rate=0.25 
            h=g*(1+rate)**f
            param=(c,d,e,a,g,b,h,j,f)
            import sqlite3
            sqliteConnection=sqlite3.connect("Bank.db")
            cursor=sqliteConnection.cursor()
            cursor.execute("INSERT INTO Loan(Name, PassportNum, AccountNum, Type, Amount, InterestType, TotalPayAtEnd, Date, Time) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", param)
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()
            print("Loan processed of:",g)
            print("To be paid by:",j)
            print("Amount to be paid by the end of the period:",h)
        if a==2:
            x="Simple Interest"
            rate=0.2
            i=g*rate*f
            y=g+i
            params=(c,d,e,a,g,x,y,j,f)
            import sqlite3
            sqliteConnection=sqlite3.connect("Bank.db")
            cursor=sqliteConnection.cursor()
            cursor.execute("INSERT INTO Loan(Name, PassportNum, AccountNum, Type, Amount, InterestType, TotalPayAtEnd, Date, Time) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()
            print("Loan processed of:",g)
            print("To be paid by:",j)
            print("Amount to be paid by the end of the period:",y)
