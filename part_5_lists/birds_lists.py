# Lists
birds = ["Pigeon", "Crow", "Barn Owl", "Goose", "Swan", "Blue Tit", "BlackBird", "Buzzard", "Egret", "Gull", "Rosefinch"]
print(birds)

# Accessing Elements in a list = [0, 1, 2, etc.]
birds = ["Pigeon", "Crow", "Barn Owl", "Goose", "Swan", "Blue Tit", "BlackBird", "Buzzard", "Egret", "Gull", "Rosefinch"]
print(birds[1])

# [1] = "Crow"

# We can make the list none captial and add .title() to it. Example print(birds[2].title()) = "Barn Owl"

birds = ["pigeon", "crow", "barn Owl", "goose", "swan", "blue tit", "blackbird", "buzzard", "egret", "gull", "rosefinch"]
print(birds[2].title())

# Index starts at 0 not 1. [0] = pigeon, [1] = crow
birds = ["pigeon", "crow", "barn Owl", "goose", "swan", "blue tit", "blackbird", "buzzard", "egret", "gull", "rosefinch"]
print(birds[0].title())
print(birds[1].title())

# Index [-1], will return to the last item in the list [-1] = rosefinch
birds = ["pigeon", "crow", "barn Owl", "goose", "swan", "blue tit", "blackbird", "buzzard", "egret", "gull", "rosefinch"]
print(birds[-1].title())

# Using a indvidual value from a list with an f string
birds = ["pigeon", "crow", "barn Owl", "goose", "swan", "blue tit", "blackbird", "buzzard", "egret", "gull", "rosefinch"]
message = f"My favourite bird is a {birds[2].title()}."
print(message)