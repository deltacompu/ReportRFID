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
sql= "SELECT DATE(date_time) AS day, building, type_asset, COUNT(*) AS count_of_records FROM tags_seen WHERE date_time >= CURDATE() - INTERVAL 8 DAY GROUP BY day, building, type_asset ORDER BY day"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()   
   for row in results:
      Date_and_time = row[0]
      Building = row[1]
      Type_asset = row[2]
      Count_of_Records = row[3]
      # Now print fetched result 
      print (Date_and_time, Building, Type_asset, Count_of_Records)
   
   body = 'The subsequent table presents the assests identified by the RFID system within the past 8 days in each Building 1\n'
   body += '\n'
   body += 'Date and time \t \t Location \t \t \t Type of Asset \t \t Amount \n'
   body += '\n'
   for line in results:
      body += "%s \t \t \t %s \t \t \t %s \t \t \t \t %s\n"% (line[0],line[1],line[2],line[3])  
   
   try:
      
      msg = MIMEText(body)
      msg['Subject'] = "Report of RFID system"
      msg['From'] = 'davsuar@amazon.com'
      msg['To'] = 'polzine@amazon.com'    
      s = smtplib.SMTP("mail-relay.amazon.com")
      s.sendmail(msg['From'], [msg['To']], msg.as_string())
      s.quit()
   
   except smtplib:
      print ("Error: unable to send email")
         
except:
   print ("Error: unable to fetch data")
   
# disconnect from server
db.close()