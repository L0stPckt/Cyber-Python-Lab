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
    message = input("Enter a message to encrypt: ")
    shift = int(input("Enter a shift number from 1 to 24: "))
    print("Message:", message)
    print("Shift: ", shift)
elif choice == "2":
        print("Decrypt selected")
elif choice == "3":
      print("Brute Force selected")
elif choice =="4":
      print("Exiting ..")
else:
      print("Invalid selection. Please enter a number between 1 and 4")