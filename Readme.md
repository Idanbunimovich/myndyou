#Myndyou assigment
web server which responsile of uploading and fetching patients

1. orm is sqlalchemy
2. fastapi for the web server framework
3. db is sql with mysql

to use the orm crud theres the base.py under model which has the basic crud functions such as insert and save
which you can extend from new orm classes you want to implement and use the functionality 
all the controllers is placed under api controllers

theres two routes:
1. GET /patient?id= which retreives patient id status and details and phones
2. POST /patient which you can attach either json body to list patients to save or attach csv file to save the patients
