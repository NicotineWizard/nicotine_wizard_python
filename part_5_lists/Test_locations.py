# Test 1.8 = Seeing the world list

locations = ["japan", "germany", "canda", "columbia", "mexico"]

print("\nHere are the locations I'd like to visit:")
print(locations)

print("\nHere is the sorted list:")
print(sorted(locations))

print("\nHere is the orginal list:")
print(locations)

locations.reverse()
print("\nHere is the list in reverse order")
print(locations)

locations.reverse()
print("\nHere is the list back in order via reverse")
print(locations)

locations.sort()
print("\nHere are the locations in alaphabetical order:")
print(locations)

locations.sort(reverse=True)
print("\nHere are the locations in reverse-alphabetical order:")
print(locations)

print("-------------------------------------------------------------------")

# Test 1.9 = len of guest list

guest_list = ["ada lovelace", "linus torvalds", "john carmack", "grace hopper"]
personal_msg_1 = f"{guest_list[0].title()}. You are invited to my dinner party!"
personal_msg_2 = f"{guest_list[1].title()}. You are invited to my dinner party!"
personal_msg_3 = f"{guest_list[2].title()}. You are invited to my dinner party!"
personal_msg_4 = f"{guest_list[3].title()}. You are invited to my dinner party!"

print(f"{personal_msg_1}\n{personal_msg_2}\n{personal_msg_3}\n{personal_msg_4}")



print("-----------------------------------------------------")


cant_make_it = "ada lovelace"
guest_list.remove(cant_make_it)
print(f"{cant_make_it.title()}. Can not make it to the event!")

guest_list.insert(0, "alan turing")



personal_msg_1 = f"{guest_list[0].title()}. You are invited to my party!"
personal_msg_2 = f"{guest_list[1].title()}. You are invited to my party!"
personal_msg_3 = f"{guest_list[2].title()}. You are invited to my party!"
personal_msg_4 = f"{guest_list[3].title()}. You are invited to my party!"

print(f"{personal_msg_1}\n{personal_msg_2}\n{personal_msg_3}\n{personal_msg_4}")

print("------------------------------------------------------")


print(f"{personal_msg_1}\n{personal_msg_2}\n{personal_msg_3}\n{personal_msg_4}. I have found a bigger table")

guest_list.insert(0, "bill gates")
guest_list.insert(3, "ken thompson")
guest_list.append("brian kernighan")

personal_msg_1 = f"{guest_list[0].title()}. You are invited to my party!"
personal_msg_2 = f"{guest_list[1].title()}. You are invited to my party!"
personal_msg_3 = f"{guest_list[2].title()}. You are invited to my party!"
personal_msg_4 = f"{guest_list[3].title()}. You are invited to my party!"
personal_msg_5 = f"{guest_list[4].title()}. You are invited to my party!"
personal_msg_6 = f"{guest_list[5].title()}. You are invited to my party!"
personal_msg_7 = f"{guest_list[6].title()}. You are invited to my party!"

print(f"{personal_msg_1}\n{personal_msg_2}\n{personal_msg_3}\n{personal_msg_4}\n{personal_msg_5}\n{personal_msg_6}\n{personal_msg_7}")




print("-------------------------------------------------------")

print("I'm so sorry, I can only invite 2 people!")

remove_guest = guest_list.pop(0)
print(f"I'm sorry {remove_guest.title()}, You have been remove from the guest list")
remove_guest = guest_list.pop(0)
print(f"I'm sorry {remove_guest.title()}, You have been remove from the guest list")
remove_guest = guest_list.pop(1)
print(f"I'm sorry {remove_guest.title()}, You have been remove from the guest list")
remove_guest = guest_list.pop(2)
print(f"I'm sorry {remove_guest.title()}, You have been remove from the guest list")
remove_guest = guest_list.pop(2)
print(f"I'm sorry {remove_guest.title()}, You have been remove from the guest list")

final_msg_1 = f"{guest_list[0].title()}. You are still invited to my party!"
final_msg_2 = f"{guest_list[1].title()}. You are still invited to my party!"

print(len(guest_list), "guests are invited to my party!")