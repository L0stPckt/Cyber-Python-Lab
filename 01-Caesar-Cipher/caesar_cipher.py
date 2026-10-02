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

    try: #try and except were added so that if a value error occurs, such as inputing a string in the integer it allows the system to give the user an error instead of crashing
        
        shift = int(input(" Enter shift number: "))
        if 0 <= shift <=25: 

            encrypted_message = " " #creating empty string container to place new letters        

            for letter in message:
                if letter.lower() in alphabet:

                    position = alphabet.index(letter.lower())
                    new_position = (position + shift) % 26
                    new_letter = alphabet[new_position]

                    if letter.isupper():
                        new_letter = new_letter.upper()
                        #if the original letter ws uppercase, make the new letter upper case
                    
                    encrypted_message = encrypted_message + new_letter #creating a single line for the encrypted letters
        
                else:
                    encrypted_message = encrypted_message + letter
            print(encrypted_message)
        else:
            print("ERROR: Shift must be between 0 and 25") 
    
    except ValueError:
        print("ERROR: Shift must be a whole number between 0 and 25") 



elif choice == "2":
    print("Decrypt selected")
    message = input("Enter a message to decrypt: ")
    try: 
        shift = int(input(" Enter shift number: "))
            
        if 0 <= shift <=25: 
            decrypted_message = ""

            for letter in message:
                if letter.lower() in alphabet:

                    position = alphabet.index(letter.lower())
                    new_position = (position - shift) % 26
                    new_letter = alphabet[new_position]

                    if letter.isupper():
                        new_letter = new_letter.upper()
                    decrypted_message = decrypted_message + new_letter
                else:
                    decrypted_message = decrypted_message + letter
            print(decrypted_message)

        else:
            print("ERROR: Shift must be between 0 and 25")

    except ValueError:
        print("ERROR: Shift must be a whole number between 0 and 25")

elif choice == "3":
      print("Brute Force selected")
      message = input("Enter a message to Brute Force: ")

      for shift in range(26):
        decrypted_message = ""

        for letter in message:

            if letter.lower() in alphabet:
                position = alphabet.index(letter.lower())
                new_position = (position - shift) % 26
                new_letter = alphabet[new_position]

                if letter.isupper():
                    new_letter = new_letter.upper()

                decrypted_message = decrypted_message + new_letter

            else:
                decrypted_message = decrypted_message + letter

        print("Shift", shift, ":", decrypted_message)

elif choice =="4":
      print("Exiting ..")
else:
      print("Invalid selection. Please enter a number between 1 and 4")