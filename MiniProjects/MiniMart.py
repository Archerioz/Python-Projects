#Welcome To Mini Mart
price = 0.0
cart = ""

print()
print("--Welcome to MiniMart! We've Got A lot of Goods That You Can Buy--")
print()
print ("Here's a list of our Items:")
print("------------------------------")
print("-Apples", "-Oranges","-Bananas","-Mangos")
print("-Sprite", "-Fanta","-Coca cola","-Pepsi")
print("-Headphones", "-Computer Mice","-Keyboards","-Monitors")
print()
print("You can only choose 6, pick wisely!")
print()

name = input("Before You Shop, what's your name? ")
print("Nice to meet you,", name + "!")
print()


cart += input("What's your first item?: ") + ", "
price += 3.1
print()

cart += input("What's your second item?: ") + ", "
price += 4.3
print()

cart += input("What's your third item?: ") + ", "
price += 2.5
print()

cart += input("What's your fourth item?: ") + ", "
price += 8.6
print()

cart += input("What's your fifth item?: ") + ", "
price += 7.7
print()

cart += input("What's your sixth item?: ") + ", "
price += 9.1
print()

print("You've bought : ", cart + ". Final Price: ", price)
print()

print("Thank You for Visiting MiniMart. See you Soon!")