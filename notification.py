#!/usr/bin/python3
import pymysql
from pprint import pprint
import re
import smtplib
from email.mime.text import *
# Open database connection
db = pymysql.connect(host="localhost",user="userRFID",password="Amazon2022!",db="socka" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql= "select model, date_time, building from tags_seen where date_time > now() - interval 12 hour"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   '''
   for row in results:
      ID = row[0]
      Image = row[1]
      ID_EPC = row[2]
      Type_of_asset = row[3]
      Model = row[4]
      Date_and_time = row[5]
      Building = row[6]
      # Now print fetched result   
      print (ID, Image, ID_EPC, Type_of_asset, Model, Date_and_time, Building )
   
   '''
   for row in results:
      Date_and_time = row[0]
      Type_of_asset = row[1]
      Building = row[2]
      # Now print fetched result 
      print (Date_and_time, Type_of_asset, Building)
   
   body = 'The following is a list of equipments detected by the RFID system in the last 24 hours \n'
   body += '\n'
   body += 'Date and time \t \t Type of asset \t Building \n'
   body += '\n'
   for line in results:
      body += "%s \t %s \t \t %s\n"% (line[0],line[1],line[2])
   
   try:
      
      msg = MIMEText(body)
      msg['Subject'] = "Report of RFID system"
      msg['From'] = 'davsuar@amazon.com'
      msg['To'] = 'davsuar@amazon.com'    
      s = smtplib.SMTP("mail-relay.amazon.com")
      s.sendmail(msg['From'], [msg['To']], msg.as_string())
      s.quit()
   
   except smtplib:
      print ("Error: unable to send email")
         
except:
   print ("Error: unable to fetch data")
   
# disconnect from server
db.close()