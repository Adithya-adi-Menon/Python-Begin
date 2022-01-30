#Dictionary - key/value pair {} 

drink = { "white Russian": 7, "Old fashion ":10,"Lemon drop":8}
#Key and Value
print(drink)


employees = {"Finance":["Bob","Linda", "Tina"], "IT":["Gene", "Louise","Teddy"],"HR":["Jimmy","jr","Mort"]}

print (employees)

employees["Legal"] = ["Mr.Fond"] #add new key: value pair
print(employees)

employees.update({"Sales":["Andie", "Ollie"]})
print(employees)

drink['white Russian'] = 8
print(drink)

print(drink.get("white Russian"))