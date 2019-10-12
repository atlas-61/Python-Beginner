# -*- coding: utf-8 -*-
import sqlite3 as sql


def selectOperations():
    connection = sql.connect("chinook.db")
    cursor = connection.execute("select * from customers")
    
    for row in cursor:
        print("First name: ", row[1])
     #when we use " three times it s possible to split string   
    cursor = connection.execute("""select FirstName, LastName 
                                from customers 
                                where city = 'Prague' or city = 'Berlin'
                                order by FirstName desc""")
    
    for row in cursor:
        print("* * * * * * * * *")
        print("Person: ", row)
    
    cursor = connection.execute("""select city, count(*) from customers
                                group by city
                                having count(*) > 1
                                order by count(*)""")
    for row in cursor:
        print("* * * * * * * * *")
        print("City: ", row[0])
        print("Count: ", row[1])
    
    cursor = connection.execute("""select FirstName, LastName 
                                from customers 
                                where FirstName like 'a%' """)
    
    for row in cursor:
        print("* * * * * * * ")
        print("First name: ", row[0])
        
    connection.close()
    
#selectOperations()    

def insertCustomer():
    connection = sql.connect("chinook.db")
    connection.execute("""insert into customers 
                       (firstName,lastName,city,email)
                       values ('Booker','Dewitt','Colombuia','booker@yahoo.com')""")
    connection.commit()

    connection.close()
    
#insertCustomer()

def updateCustomer():
    connection = sql.connect("chinook.db")
    connection.execute("""update customers set city='Rapture'
                       where firstName = 'Booker'""")
    
    connection.commit()

    connection.close()
    
#updateCustomer()

def deleteCustomer():
    connection = sql.connect("chinook.db")
    connection.execute("""Delete from customers
                       where customerid = 59 """)
    
    connection.commit()

    connection.close()
    
#deleteCustomer()

def joinOperations():
    connection = sql.connect("chinook.db")
    cursor = connection.execute("""select albums.Title, 
                                artists.Name from artists
                                inner join albums on 
                                artists.ArtistId = albums.ArtistId""")
    
    for row in cursor:
        print("Title: ", row[0] + " Name: ", row[1])
       

    connection.close()

joinOperations()
