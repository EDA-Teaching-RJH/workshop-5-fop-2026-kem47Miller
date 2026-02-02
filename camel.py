name=str(input("What is your name in camelCase? "))
snake_case=""
for char in name:
    if char.isupper():
        snake_case += '_' + char.lower()
    else:
        snake_case += char
print(snake_case)
