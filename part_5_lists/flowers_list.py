# Modifying, Adding and Removing Elements

flowers = ["Acacia", "Daisy", "Begonia"]
print(flowers)

flowers[0] = "Bellflower"
print(flowers)

# When running this, it won't add "BellFlower" to the list
# Append list by = .append("BellFlower")

flowers.append("Bellflower")
print(flowers)

# .append allows us to build upon the list dynamically

flowers.append("Camellia")
flowers.append("Lily")
flowers.append("Daisy")

# Insert elements into a list = .insert[]

flowers.insert(0, "Dandelion")
print(flowers)

# Removing elements = del [] we can remove any item from the list 0-9

del flowers[1]
print(flowers)

# Removing an item using pop()
# This will remove the last item but keep the value, and move it from the list
# This will remove "Daisy"

popped_flowers = flowers.pop()
print(flowers)
print(popped_flowers)

# We cam use pop with an f string to make a simple sentence
# The last flower I smelt was a Lilly

last_smelt = flowers.pop()
print(f"The last flower I smelt was {last_smelt.title()}.")

# We can use pop for any item in the list .pop(0)
# The first flower I owned was a "Dandelion"

first_flower = flowers.pop(0)
print(f"The first flower I owned was a {first_flower.title()}.")