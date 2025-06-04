
n = int(input("Enter a number: "))

print("\nEven numbers up to", n, ":")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\n\nOdd numbers up to", n, ":")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")