num = int(input(" Which number table do you need?"))

print(f"\n=== table of {num}===")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("=== 1 to 10 ===")
for n in range(1, 11):
    print(f"\n table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
