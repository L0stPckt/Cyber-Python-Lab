alphabet = "abcdefghijklmnopqrstuvwxyz"

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
    shift = int(input(" Enter shift number: "))
    if 0 <= shift <=25: 

        for letter in message:
            if letter.lower() in alphabet:

                position = alphabet.index(letter.lower())
                new_position = (position + shift) % 26
                new_letter = alphabet[new_position]

                if letter.isupper():
                     new_letter = new_letter.upper()
                    #if the original letter ws uppercase, make the new letter upper case
                print(new_letter)
       
            else:
                 print(letter)    

     
    else:
        print("ERROR: Shift must be between 0 and 25") 


elif choice == "2":
        print("Decrypt selected")
elif choice == "3":
      print("Brute Force selected")
elif choice =="4":
      print("Exiting ..")
else:
      print("Invalid selection. Please enter a number between 1 and 4")