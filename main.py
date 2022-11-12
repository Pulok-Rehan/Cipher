alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    if direction == "encode":
        new_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                if new_position >= len(alphabet):
                    new_position = new_position - len(alphabet)
                new_letter = alphabet[new_position]
                new_text += new_letter
            else:
                new_text+=letter


        print(f"the encrypted word is {new_text}")
    elif direction == "decode":
        new_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift
                if new_position < 0:
                    new_position = len(alphabet) + new_position
                new_letter = alphabet[new_position]
                new_text += new_letter
            else:
                new_text+= letter


        print(f"The decrypted text is {new_text}")
    else:
        print("Please choose either encode or decode")

should_continue= True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift= shift%26
    caesar(text, shift, direction)
    yes_or_no= input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    if yes_or_no=='no':
        should_continue=False
        print("Thank for using caesar cipher")



