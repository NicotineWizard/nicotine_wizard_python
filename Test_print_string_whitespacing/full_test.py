# full test_print_string_whitespacing

# 0.3 = personal message

name = "john"
learn = "lets learn python"
full_message = f"{name} {learn}"
print(f"Hello {full_message} today!")

# 0.4 = name cases

name_1 = "john smith"
print(name_1.lower())
print(name_1.upper())
print(name_1.title())


# 0.5 = famous quote

print('Linus Torvald once said, "Talk is cheap, show me the code"')


# 0.6 = famous quote 2 - with a print variable

famous_person = 'Linus Torbald once said, "Talk is cheap, show me the code"'
print(famous_person)

# 0.7 = stripping name \t with removal of spacing

first_name = " jane "
last_name = " doe "
full_name = f"{first_name} {last_name}"

clean_first = first_name.replace(" ", "")
clean_last = last_name.replace(" ", "")
full_name = f"{clean_first} {clean_last}"

print(f"\t{full_name}")
print(f"\n{full_name}")

# 0.8 remove suffix ".txt"

file_ext = "python_notes.txt".removesuffix(".txt")
print(file_ext)