

students = [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("David", 85)]
students.sort(key=lambda x: x[1])
print("Sorted list:", students)

# Output:
# Sorted list: [('Bob', 72), ('David', 85), ('Alice', 88), ('Charlie', 95)]
