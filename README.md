# Project-2020---Data-Representation-and-Querying
![schema](Images/schema.jpg)


## Scope
To provide a web page served by a web application that communicates to a server. The server should contain static pages and an app server which uses CRUD operations on a database. 
[See here for instructions](Project Description.pdf)

A rehash of the sample project lab, I will do in
Topic09-linking to db, but with your own data.
I.e.:
1. A basic Flask server that has a
2. REST API, (to perform CRUD operations)
3. One database table and
4. Accompanying web interface, using AJAX
calls, to perform these CRUD operations

## Desciption
This project will implement an app server to deal with patients admitted to a hospital. A database of patients will be stored on a remote server and will be accessed via a web page and app server. Below decribes the architecture involved in providing this solution ![architecture](Images/Architecture.jpg).

At the heart of this solution will be an App server, run using FLASK package in python, which will communicate with the browser using HTTP protocol. This will be used to serve any static web pages, in html, from the server onto the browser. From the browser, a user can issue specific requests. These requests will be sent up to the server in JSON format using AJAX calls. 

A file on the server, named server.py, will take all possible requests and map each one to a particular function and return back responses. A DAO file will use MySql connector to connect from server.py to the database and perform the necessary CRUD operations on the database and return data back to the server. It will also convert the data from a tuple to JSON. The project will also include the .sql file containing the SQL used to create the database being used for the project. 
