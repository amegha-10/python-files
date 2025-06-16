#program using loops

# 1.For loop

print("1.For loop:")
for i in range(1, 6):
    print(i)

# 2.While loop

print("\n2.While loop:")
i = 1
while i <= 5:
    print(i)
    i = i + 1

# 3.Nested loop

print("\n3.Nested loop:")
for i in range(3):
    for j in range(3):
        print("(", i, ",", j, ")", end=" ")
    print()

# 4.Loop with break

print("\n4.Loop with break:")
for i in range(1, 6):
    if i == 3:
        print("Break at", i)
        break
    print(i)

# 5.Loop with continue

print("\n5.Loop with continue:")
for i in range(1, 6):
    if i == 3:
        print("Skip", i)
        continue
    print(i)
