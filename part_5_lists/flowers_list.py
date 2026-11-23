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