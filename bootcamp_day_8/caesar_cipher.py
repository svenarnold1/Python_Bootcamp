from caesar_cipher_add import alphabet, logo

print(logo)
keep_running = True
while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))

# avoid errors caused by shift
    shift = shift % 26

# this is a function that encrypt text or decrypts hidden text
    def caesar(input_text, shift_amount, cipher_direction):
        output_text = ""
        if cipher_direction == 'decode':
            shift_amount *= -1
            for letter in input_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position + shift_amount
                    new_letter = alphabet[new_position]
                    output_text += new_letter
                else:
                    output_text += letter
        return f"the {direction}d message is: {output_text}"


    if direction != 'encode' and direction != 'decode':
        print("You chose an invalid operation!")
    else:
        print(caesar(text, shift, direction))
        again = input("if you want to continue, type 'yes', type 'no' if you want to quit:\n").lower()
        if again == 'no':
            keep_running = False

    # def encrypt(plain_text, shift_amount):
    #    cypher_text = ""
    #    for letter in plain_text:
    #      position = alphabet.index(letter)
    #      new_position = position + shift_amount
    #      new_letter = alphabet[new_position]
    #      cypher_text += new_letter
    #    return f"The encoded text is {cypher_text}"

    # def decrypt(encrypted_text, shift_amount):
    #   plain_text = ""
    #   for letter in encrypted_text:
    #       position = alphabet.index(letter)
    #       new_position = position - shift_amount
    #       new_letter = alphabet[new_position]
    #       plain_text += new_letter
    #   return f"The decrypted text is {plain_text}"

    # Eof (End of File)
