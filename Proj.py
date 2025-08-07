#Variable names cannot start with a digit, but can start with an underscore or letter

print("sup")
x = "hello"
y = "world"
print(x +" "+ y)
print(type(x))
print(isinstance(x,str))
print()

apple = banana = grape = "fruit" #Assign something to multiple variables
print(apple)
print(banana)
print(grape)
print()

print(apple, "!")
print(banana, "!?!")
print(grape, "!??!")
print()

print(apple, banana, grape)
print(banana, grape, apple)
print(grape, apple, banana)
print()

print(5 + 2.0)
print(type(5 + 2.0)) #Adding the float to the int converts it to a float

#input
favColor = input("What's your favorite Color?: ")
print(favColor, "Is my favorite color too!") #or I can also concatenate with print(favColor + " " + "Is my favorite color too!")
