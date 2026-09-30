print("===================================")
print("       CAESAR CIPHER TOOL")
print("===================================")
print()
print("Welcome to the Casear Cipher Tool")
print()
print("Enter [1] for Encrypt")
print("Enter [2] for Decrypt")
print("Enter [3] for Brute Force")
print("Enter [4] to Exit")

choice = input("Select an option ")

if choice == "1": 
    print("Encrypt selected")
elif choice == "2":
        print("Decrypt selected")
elif choice == "3":
      print("Brute Force selected")
elif choice =="4":
      print("Exiting ..")
else:
      print("Please enter a number between 1 and 4")