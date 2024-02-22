# qstream
Qstream Python Test

## Question 1:
I have created the function sum_pair() to return the list of indexes 
that the values addition is equal to  target


## Question 2:
I have utilized the recursion as we would not know the layers of nested lists

## Question 3:
I have utilized python web frameqork Flask with in built database sqlite
if you have Linux distribution you can use "curl" to test the code:

### Following commands will give you erros: 

$ curl -X POST -H "Content-Type: application/json" -d '{"data": {"attributes": {"last_name": "Jadhav","email_address": "Swapnali@example.com", "country": "United States"}}}'   http://127.0.0.1:5000/users

$ curl -X POST -H "Content-Type: application/json" -d '{"data": {"attributes": {"first_name": "Swapnali", "email_address": "Swapnali@example.com", "country": "United States"}}}'   http://127.0.0.1:5000/users

$ curl -X POST -H "Content-Type: application/json" -d '{"data": {"attributes": {"first_name": "Swapnali", "last_name": "Jadhav", "country": "United States"}}}'   http://127.0.0.1:5000/users



### Following commands will execute successfully (POST):
$ curl -X POST -H "Content-Type: application/json" -d '{"data": {"attributes": {"first_name": "Swapnali", "last_name": "Jadhav","email_address": "Swapnali@example.com", "country": "United States"}}}'   http://127.0.0.1:5000/users

$ curl -X POST -H "Content-Type: application/json" -d '{"data": {"attributes": {"first_name": "Swapnali", "last_name": "Jadhav","email_address": "Swapnali@example.com"}}}'   http://127.0.0.1:5000/users

### Following commands will retrieve the users data
$ curl http://127.0.0.1:5000/users

$ curl http://127.0.0.1:5000/users?sort=last_name

You can sort the data with other fields as well