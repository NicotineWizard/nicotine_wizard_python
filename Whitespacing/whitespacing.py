# whitespacing, add a tab to text = \t

print("Hello Python")

print("\tHello Python")

# whitespacing, add a new line to text = \n

print("Languages:\nPython\nC\nJavaScript")

# whitespacing, add a tab and new line to text

print("Languages:\n\tPython\n\tC\n\tJavascript")

# removing prefixes = .removeprefix

web = "https://www.bbc.co.uk".removeprefix("https://")
print(web)


# remove whitespacing/ space before and after "python". lstrip = remove from left, rstrip = remove from right

language = " Python "
print(language)

language = " Python "
res = language.lstrip()
print(res)
