import randoms
letters = ["A", "B", "c", "D", "E", "F"]
symbols = ["&", "*", "%", "#"]
numbers = [1, 3, 4]
print("Welcome to my password generator")
letters = int(input("Enter how many letters you want?\n"))
symbols = int(input("How many symbols do you want?\n"))
numbers = int(input("How many numbers do you want?\n"))

#password_list = []

#for char in range(1, letters +1):
 #   password_list.append(random.choice(letters))

#for char in range(1, numbers +1):
 #   password_list.append(random.choice(numbers))

#for char in range(1, symbols +1):
 #   password_list.append(random.choice(symbols))

#print(password_list)
#random.shuffle(password_list)
#print(password_list)

#password = ""
#for char in password_list:
 #   password +=char

#print(f"Your password is; {password}")

password = ""
for char in range (1, letters +1):
    password +=randoms.choice(letters)

for char in range (1, numbers +1):
    password +=randoms.choice(numbers)

for char in range (1, symbols +1):
    password +=randoms.choice(symbols)

print(password)
