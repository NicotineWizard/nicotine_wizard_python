# Test 1.4 = Guest list

guest_list = ["ada lovelace", "linus torvalds", "john carmack", "grace hopper"]
personal_msg_1 = f"{guest_list[0].title()}. You are invited to my dinner party!"
personal_msg_2 = f"{guest_list[1].title()}. You are invited to my dinner party!"
personal_msg_3 = f"{guest_list[2].title()}. You are invited to my dinner party!"
personal_msg_4 = f"{guest_list[3].title()}. You are invited to my dinner party!"

print(f"{personal_msg_1}\n{personal_msg_2}\n{personal_msg_3}\n{personal_msg_4}")

# Test 1.5 = Changing guest list

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

# Test 1.6 = More guests!

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


# Test 1.7 = Remove guests, using pop, then delete to empty the list

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

print(f"{final_msg_1}\n{final_msg_2}")

del guest_list[0]
del guest_list[0]

print(guest_list)

# final result and empty list