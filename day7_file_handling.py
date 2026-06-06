print("===Day 7 file handling on phone===")

file = open("salary.txt","w")
file.write("Ramla\n")
file.write("fresher\n")
file.write("500000yen\n")
file.write("Tokyo\n")
file.close()
print("salary.txt created by Ramla-san")
  
file = open("salary.txt","r")
data = file.readlines()
file.close()
  
print("\nHR data from tokyo")
print("Name:",data[0].strip())
print("position:",data[1].strip())
print("salary:",data[2].strip())
print("location:",data[3].strip())
  
print("\nfile reading complete. otsukaresama!")
