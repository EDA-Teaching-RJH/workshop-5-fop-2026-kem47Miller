# This program converts a valid camelCase variable name to snake_case.
# It performs full validation to ensure the input is safe before processing.

name = input("What is your name in camelCase? ").strip()

# Edge case: empty input
if not name:
    print("Invalid input: name cannot be empty.")
    exit()

# Edge case: camelCase variables must start with a lowercase letter.
# An uppercase first letter would indicate PascalCase instead.
if not name[0].islower():
    print("Invalid input: camelCase must start with a lowercase letter.")
    exit()

# Edge case: if the input already contains underscores, it is not camelCase
# and converting it again could produce incorrect results.
if "_" in name:
    print("Invalid input: input must be camelCase, not snake_case.")
    exit()

# Edge case: check if name is alphanumeric (allowing only letters for simplicity)
if not name.isalpha():
    print("Invalid input: variable names must contain letters only.")
    exit()

# Edge case: check if contains uppercase letters (otherwise it's already snake_case)
if not any(char.isupper() for char in name[1:]):
    print("Invalid input: camelCase should contain at least one uppercase letter after the first.")
    exit()

snake_case = ""

# Edge case: this loop assumes every uppercase letter marks a word boundary.
# Unexpected characters could break this logic if validation was removed.
for char in name:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

print(snake_case)






#name=str(input("What is your name in camelCase? "))
#snake_case=""
#for char in name:
    #if char.isupper():
        #snake_case += '_' + char.lower()
    #else:
        #snake_case += char
#print(snake_case)
