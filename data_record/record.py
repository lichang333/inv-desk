#!/usr/bin/python
import json


a_file = open("sample_file.json", "r")
json_object = json.load(a_file)
a_file.close()
print(json_object)


json_object[0]["volume"] = 1000
# best_otc_price = (json["data"][0]["price"])

a_file = open("sample_file.json", "w")
json.dump(json_object, a_file)
a_file.close()




  
## appen json object      
      
# with open('data.json') as json_file: 
#     data = json.load(json_file) 
      
#     temp = data['emp_details'] 
  
#     # python object to be appended 
#     y = {"emp_name":'Nikhil', 
#          "email": "nikhil@geeksforgeeks.org", 
#          "job_profile": "Full Time"
#         } 
  
  
#     # appending data to emp_details  
#     temp.append(y) 
      
# write_json(data) 