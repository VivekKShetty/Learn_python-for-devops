My_Dict = {"Name": "Virat", "Age": "28", "City": "Bangalore" }
print(My_Dict)                #Output is {'Name': 'Virat', 'Age': '28', 'City': 'Bangalore'}
print(My_Dict["Name"])        #Output is Virat

print(My_Dict.get("Century"))  #output is None instead of getting error
print(My_Dict.get("Century", {}))  #output is {}