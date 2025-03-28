def transform_to_binary(text):
    binary_result = ""
    for char in text:
        binary_result += format(ord(char), '08b') + " "
    return binary_result.strip()

def transform_number_to_binary(number):
    try:
        num = int(number)
        if num < 0:
            raise ValueError("The number must be positive.")
        return format(num, 'b')
    except ValueError:
        return None

def binary_to_text(binary):
    text_result = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        decimal = int(byte, 2)
        text_result += chr(decimal)
    return text_result

def is_valid_frase(frase):
    if any(char.isdigit() for char in frase):
        return False
    return True

def is_valid_number(numero):
    if any(char.isalpha() for char in numero):
        return False
    return True

def is_valid_binary(binary):
    return all(char in '01' for char in binary) and len(binary) % 8 == 0

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_input(message, validation_func):
    while True:
        user_input = input(message).strip()
        if validation_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

def menu():
    clear_screen()
    print("Choose an option:")
    print("1. Convert a phrase to binary")
    print("2. Convert a number to binary")
    print("3. Translate a binary number to text")
    print("4. Exit")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        print("\nYou chose to convert a phrase to binary.")
        print("Rules: No numbers are allowed in the phrase.")
        frase = get_valid_input("Enter a phrase: ", is_valid_frase)
        print("Binary representation:", transform_to_binary(frase))

    elif choice == '2':
        print("\nYou chose to convert a number to binary.")
        print("Rules: No letters are allowed in the number.")
        numero = get_valid_input("Enter a number: ", is_valid_number)
        binario = transform_number_to_binary(numero)
        if binario is None:
            print("Error: Invalid input. Please try again.")
        else:
            print(f"Number {numero} in binary:", binario)

    elif choice == '3':
        print("\nYou chose to translate a binary number to text.")
        print("Rules: The binary must only contain 0s and 1s, with no spaces between the digits, and the length must be a multiple of 8.")
        while True:
            binary = get_valid_input("Enter a binary number (no spaces between digits): ", is_valid_binary)
            if not is_valid_binary(binary):
                print("Error: Binary must only contain 0s and 1s, and its length must be a multiple of 8. Please try again.")
            else:
                text = binary_to_text(binary)
                print(f"Text corresponding to the binary '{binary}': {text}")
                break

    elif choice == '4':
        print("Exiting... See you soon!")
        exit()

    else:
        print("Invalid option! Please try again.")
    
    input("Press Enter to continue...")
    menu()

menu()
