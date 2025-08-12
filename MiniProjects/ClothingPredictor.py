print()
print("---CLOTHING PREDICTOR---")
print()

temperature = int(input("What's the current temperature of where your're living?: "))

if temperature >= 85:
    print("It's pretty hot, wear shorts and a t-shirt.")
elif temperature >= 65:
    print("A light jacket should get the job done.")
elif temperature >= 45:
    print("The temperature is chilly, wear a sweater.")
else:
    print("It's cold! wear a coat, scarf, gloves, and anything else to protect yourself from the cold.")