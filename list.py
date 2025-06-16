
colors = ["red", "blue", "green"]
print("\nList:", colors)


colors.append("yellow")
print("\nList after adding yellow:", colors)


colors.insert(1, "orange")
print("\nList after inserting orange at position 1:", colors)


colors.remove("blue")
print("\nList after removing blue:", colors)


colors.pop()
print("\nList after removing last item:", colors)


colors.sort()
print("\nSorted list:", colors)


colors.reverse()
print("\nReversed list:", colors)


print("\nTotal items on the List :", len(colors))


print("\nPosition of color red :", colors.index("red"))


print("\nHow many reds are on the list :", colors.count("red"))
