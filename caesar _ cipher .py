alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (orignal_text, shift_count):
    cipher_text = ""
    for  letters in orignal_text:
        if letters in alphabet:
            position = alphabet.index(letters)
            new_position = position + shift_count
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letters
    print(f"The encoded text is {cipher_text}")      

def decrypt (cipher_text, shift_count):
    orignal_text = ""
    for letters in cipher_text:
        if letters in alphabet:
            updated_position = alphabet.index(letters)
            updated_position = updated_position - shift_count
            updated_letter = alphabet[updated_position]
            orignal_text += updated_letter
        else:
            orignal_text += letters
    print(f"The orignal text is {orignal_text} ")

if direction == 'encode':
    encrypt(orignal_text=text, shift_count=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_count= shift)


