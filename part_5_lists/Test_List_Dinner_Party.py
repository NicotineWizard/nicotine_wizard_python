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
print(guest_list)
print(f"{cant_make_it.title()}. Can not make it to the event!")

guest_list.insert(0, "alan turing")

print(guest_list)

personal_msg_1 = f"{guest_list[0].title()}. You are invited to my dinner party!"
personal_msg_2 = f"{guest_list[1].title()}. You are invited to my dinner party!"
personal_msg_3 = f"{guest_list[2].title()}. You are invited to my dinner party!"
personal_msg_4 = f"{guest_list[3].title()}. You are invited to my dinner party!"

print(f"{personal_msg_1}\n{personal_msg_2}\n{personal_msg_3}\n{personal_msg_4}")

print("------------------------------------------------------")

