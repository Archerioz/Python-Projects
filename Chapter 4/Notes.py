#This is a single line comment that I have been using previously
num = 1 + \
      2 + \
      3 + \
      4 + \
      343 + \
      523423

print(num)

#Version where it's whithin parentheses
num = (
      1 +
      2 + 
      3 + 
      4 + 
      343 +
      523423
      )
print(num)
print()
#Conditional Statements

#Use 4 spaces to seperate different indentation levels
disaster = True
if disaster:
    print("yippie")
else:
    print("Noo!")

#The "if disaster:" part is the pythonic way of checking whether disaster is true. You could also do if disaster == True:
disaster = True
if disaster == True:
    print("yippie")
else:
    print("Noo!")
print()

# ==, >=, <=, !=, >, <, Pretty much like java

#Python uses "not", "and" "or"

#The Bottom code works essentialy as lots of "and" comparisons
x = 10
print(7 < x < 23) #(7 < x) and (x < 23)
print()

#Things such as empty strings, empty tuples, empty lists, and more are considered false, so the condition "if some_type:" essentially checks whether it's full (true),

#This is much better than just combining a whole bunch of or conditions one after another. This checks if letter is present in vowels.
vowels = "aeiou"
letter = "o"
print(letter in vowels)

word = "Hello"
if letter in word:
    print(letter + " is in your word!") 



color = "Amber"
if color == "Orange":
    print("You love oranges dont you?")
elif color == "Red":
    print("Red's a pretty nice color!")
else: 
    print("I don't know what that color is")
    