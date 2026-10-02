#alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet ="Q7@bM2xK&f1!V9w;Du4#k0'P)lz5^oA8?c$yW3,F6%j.Y(r*eUgBLtNsOiHqXvGmZpJdRCEaIhTnS"

while True:

    print("===================================")
    print("       CAESAR CIPHER TOOL")
    print("===================================")
    print()
    print("Welcome to the Caesar Cipher Tool - v2.0")    
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
            if 0 <= shift <= (len(alphabet) - 1): 

                encrypted_message = "" #creating empty string container to place new letters        

                for letter in message:
                    if letter in alphabet:

                        position = alphabet.index(letter)
                        new_position = (position + shift) % len(alphabet)
                        new_letter = alphabet[new_position]
                        encrypted_message = encrypted_message + new_letter

                    else:
                        encrypted_message = encrypted_message + letter
                print(encrypted_message)
            else:
                print("ERROR: Shift must be between 0 and " + str(len(alphabet) -1 )) 
        
        except ValueError:
            print("ERROR: Shift must be a whole number between 0 and " + str(len(alphabet) -1 )) 

    elif choice == "2":
        print("Decrypt selected")
        message = input("Enter a message to decrypt: ")
        try: 
            shift = int(input(" Enter shift number: "))
                
            if 0 <= shift <= (len(alphabet) - 1): 
                decrypted_message = ""

                for letter in message:
                    if letter in alphabet:
                        position = alphabet.index(letter)
                        new_position = (position - shift) % len(alphabet)
                        new_letter = alphabet[new_position]
                        decrypted_message = decrypted_message + new_letter
                    else:
                        decrypted_message = decrypted_message + letter
                print(decrypted_message)

            else:
                print("ERROR: Shift must be between 0 and " + str(len(alphabet) -1 ))

        except ValueError:
            print("ERROR: Shift must be a whole number between 0 and " + str(len(alphabet) -1 ))

    elif choice == "3":
        print("Brute Force selected")
        message = input("Enter a message to Brute Force: ")

        for shift in range(len(alphabet)):
            decrypted_message = ""

            for letter in message:

                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = (position - shift) % len(alphabet)
                    new_letter = alphabet[new_position]

                    decrypted_message = decrypted_message + new_letter

                else:
                    decrypted_message = decrypted_message + letter

            print("Shift", shift, ":", decrypted_message)

    elif choice =="4":
        print("Exiting ...")
        break
    else:
        print("Invalid selection. Please enter 1, 2, 3 or 4")