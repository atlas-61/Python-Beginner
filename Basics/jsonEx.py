# -*- coding: utf-8 -*-
import json
data = '{"first name": "Ricky", "last name": "Casu"}' # ' just for string and it s a json data
y = json.loads(data)
print(y["first name"])

customer = {
        "firstName": "Niki",
        "lastName": "Lauda",
        "email": "nikilauda@gmail.com"
        }
customerJson = json.dumps(customer)
print(customerJson)