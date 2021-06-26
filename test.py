

# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open('setting.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
print(data["color"])
  
# Closing file
f.close()