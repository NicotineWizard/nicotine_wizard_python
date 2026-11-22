# Test_1.1 = list of friends
friends = ["John Smith", "Jane Doe", "Alan Carter", "Emily Rose", "Deborah Hills", "Scott Townsend", "Ryan Matthews"]
print(friends)

# Test_1.2 = Greetings with the list personal message for each
friends = ["john smith", "jane doe", "alan carter", "emily rose", "deborah hills", "scott townsend", "ryan matthews"]
print(f"Hello, {friends[0].title()}, it was lovely to see you today")
print(f"You have a lovely outfit {friends[1].title()}")
print(f"{friends[2].title()}, you ran so fast today")
print(f"{friends[3].title()}, let's meet for lunch today?")
print(f"Good morning, {friends[4].title()}, I hope you have a wonderful day")
print(f"{friends[5].title()}, come see me in my office")
print(f"YOU ARE FIRED {friends[6].upper()}")

# Test_1.3 = Favourite mode of transport/make a list of statements for each

transport = ["car", "trains", "bicycle"]
print(f"{transport[0].title()}, I enjoy this as I get to hangout with friends and listen to music")
print(f"I like {transport[1].title()}, as I get to watch the counrtyside go by")
print(f"I enjoy using a {transport[2].title()}, as I can stay fit and healthly while travelling")