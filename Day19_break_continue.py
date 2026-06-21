

print("=== PART 1: break - Loop Nirthunna Button ===")

pin = "2026"

for attempt in range(1, 4):
    user_pin = input(f"Attempt {attempt}: PIN enter cheyyu: ")
    if user_pin == pin:
        print("Access Granted! Welcome Ramla")
        break  
    else:
        print("Wrong PIN")
else:

    print("Card Blocked!")

print("---")

print("\n=== PART 2: continue - Ee Round Skip Cheyyum ===")

laptops = ["i3", "i5 8th Gen", "Pentium", "i5 8th Gen", "Celeron"]

for lap in laptops:
    if lap != "i5 8th Gen":
        continue 
    print("Boss Laptop Found:", lap)

print("---")

print("\n=== PART 3: my task - i5 SPEED TEST ===")
print("1 to 20, stop on 13:")
for n in range(1, 21):
    if n == 13:
        break 
    print(n)

print("---")

print("1 to 10, odd numbers mathi:")
for n in range(1, 11):
    if n % 2 == 0:
        continue  
    print("Odd number:", n)

print("\nDay19 Complete! i5 8th Gen Rocking 🔥")
