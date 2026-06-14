password = ""

while password != "kochi123":
    password = input("Enter password: ")
    if password != "kochi123":
        print("Wrong! Try again ")

print("Correct! Welcome Kochi Queen ")



num = 7
guess = 0

while guess != num:
    guess = int(input("Guess a number 1-10: "))
    if guess < num:
        print("Go higher 🗿")
    elif guess > num:
        print("Go lower 😅")

print("You got it! It was 7 👏")
