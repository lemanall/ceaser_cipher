alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(start_text, cipher_shift,cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        cipher_shift *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + cipher_shift) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)


    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != 'yes':
        should_continue = False
        print("Goodbye!")