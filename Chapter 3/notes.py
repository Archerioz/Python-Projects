print(bool(1))

print(bool(0.8))

print(bool(3.25))

print(bool(342))

print(bool(999))

print(bool(0))

print(bool(0.000000))
print()

x = 0.0
y = 0

print(bool(x))
print(bool(y))

print(bool(x), bool(y))
print(bool(y), bool(x))
print()

#Note: Ints are not allowed to have commas, but you can use an underscore to visually seperate digits. 
z = 1_000
print(x)

w = 1_000_000
print(x)

print(3 + 3 + 5 + 3)

print(9 * 4 * 6)

print(83 * 34)

print(3 - 3 + 5 + 7)

print(9 - 4 - 6)

print(5 * 5 - 1)

print(5 / 5)

print(5 * 10 / 2)
print()

#Comparison 
print(5 / 2)
print(5 // 2) #Removes the Remainder and returns an Int

#Dividing by 0 results in a Python Exception 
#print(23 / 0) : "ZeroDivisionError"

a = 314
a -= 314
print(a)

a += 1

a += 2

a += 3

print(a)

# x = 10
# x /= 2 results in x getting 5
# x //= 3 would result in 3 being the new value for x as the decimal is just completelly removed with double slashes.

#Modulus returns remainder "%"

z = 6 % 5
print(z)

#The divmod() function gives the truncated (// not /) quotient and the remainder (%) at the same time
#divmod(8,3) : (2,2)

print(divmod(8,3))

#WIP, More tomorrow!