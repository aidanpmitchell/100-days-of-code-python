from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

option = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

message = input("Type your message: \n")

shift_number = int(input("Type the shift number: "))

def encode_message(message, shift_number):
    encoded_list = []
    for letter in message:
        original_index = alphabet.index(letter)
        new_index = original_index + shift_number
        encoded_list.append(alphabet[new_index])
    return ''.join(encoded_list)

def decode_message(message, shift_number):
    encoded_list = []
    for letter in message:
        original_index = alphabet.index(letter) + 26
        new_index = original_index - shift_number
        encoded_list.append(alphabet[new_index])
    return ''.join(encoded_list)

if option == "encode":
    encoded_result = encode_message(message, shift_number)
    print(f"Here's the encoded result: {encoded_result}")
elif option == "decode":
    decoded_result = decode_message(message, shift_number)
    print(f"Here's the decoded result: {decoded_result}")
else:
    print("That is not one of the options.")