def Encrypt(text, shift):
    encrypted_text = ""
    alphabets = ["!", "\\", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5",
    "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
    for alpha in text:
    	if alpha in alphabets:
            position = alphabets.index(alpha)
            new_position = (position + shift) % len(alphabets)
            encrypted_text += alphabets[new_position]

    return encrypted_text

def Decrypt(text, shift):
    decrypted_text = ""
    alphabets = ["!", "\\", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5",
    "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
    for alpha in text:
    	if alpha in alphabets:
            position = alphabets.index(alpha)
            new_position = (position - shift) % len(alphabets)
            decrypted_text += alphabets[new_position]

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
