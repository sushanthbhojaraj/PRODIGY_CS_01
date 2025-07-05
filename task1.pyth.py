def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
    
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("==== Caesar Cipher Tool ====")
    choice = input ("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print ("Invalid choice. Please choose 'E' or 'D'.")
        return
    
    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == 'E':
        result = caesar_encrypt(message, shift)
        print(f"\n🔐 Encrypted message: {result}")
    else:
        result = caesar_decrypt(message, shift)
        print(f"\n🔓 Decrypted message: {result}")

if __name__ == "__main__":
    main()

