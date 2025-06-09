
# Arithmetic Operators
a = 10
b = 3
print ("a=",a)
print ("b=",b)
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("\nComparison Operators:")
print("a Equal b :", a == b)
print("a Not Equal b:", a != b)
print("a Greater than b :", a > b)
print("a Less than b :", a < b)
print("a Greater than or equal b :", a >= b)
print("a Less than or equal b :", a <= b)

print("\nAssignment Operators:")
x = 5
x += 2  # x = x + 2
print("x += 2:", x)
x -= 1
print("x -= 1:", x)
x *= 3
print("x *= 3:", x)
x /= 2
print("x /= 2:", x)
x //= 2
print("x //= 2:", x)
x %= 3
print("x %= 3:", x)
x **= 2
print("x **= 2:", x)

print("\nLogical Operators:")
print("and:", a > 5 and b < 5)
print("or:", a < 5 or b < 5)
print("not:", not(a < 5))

print("\nBitwise Operators:")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT (~a):", ~a)
print("Left Shift (a << 1):", a << 1)
print("Right Shift (a >> 1):", a >> 1)

print("\nMembership Operators:")
my_list = [1, 2, 3, 10]
print("10 in my_list:", 10 in my_list)
print("5 not in my_list:", 5 not in my_list)

print("\nIdentity Operators:")
c = a
d = 10
print("c is d:", c is d)
print("c is not b:", c is not b)