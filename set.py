
colors = {"red", "blue", "green"}
print("\nSet:", colors)


colors.add("yellow")
print("\nAfter adding yellow:", colors)


colors.remove("blue")
print("\nAfter removing blue:", colors)


colors.add("red")
print("\nAfter trying to add red again:", colors)


print("\nTotal items:", len(colors))


print("\nIs 'green' in set?", "green" in colors)
