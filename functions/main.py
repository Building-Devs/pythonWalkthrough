def getLowerCase(text):
	return f"Your input was {text}, the lower case version is {text.lower()}"

value = input("Enter a text: ")
print(getLowerCase(value))