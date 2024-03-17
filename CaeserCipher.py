def Encrypt(text, shift):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_text = ""

    for alpha in text:
        if alpha.lower() in alphabets:
            position = alphabets.index(alpha.lower())
            new_position = (position + shift) % len(alphabets)
            if alpha.isupper():
                encrypted_text += alphabets[new_position].upper()
            else:
                encrypted_text += alphabets[new_position]
        else:
            encrypted_text += alpha

    return encrypted_text

def Decrypt(text, shift):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decrypted_text = ""

    for alpha in text:
        if alpha.lower() in alphabets:
            position = alphabets.index(alpha.lower())
            new_position = (position - shift) % len(alphabets)
            if alpha.isupper():
                decrypted_text += alphabets[new_position].upper()
            else:
                decrypted_text += alphabets[new_position]
        else:
            decrypted_text += alpha

    return decrypted_text

while True:
    user_choice = input("What do you want to do encrypt/decrypt/exit? ")

    if user_choice == "encrypt":
        encrypted_message = Encrypt(input("Enter the text you want to encrypt: "), int(input("Enter the shift number: ")))
        print(f"Encrypted Message: {encrypted_message}")

    elif user_choice == "decrypt":
        decrypted_message = Decrypt(input("Enter the text you want to decrypt: "), int(input("Enter the shift number: ")))
        print(f"Decrypted Message: {decrypted_message}")

    elif user_choice == "exit":
        break

    else:
        print("Enter a valid choice :)")