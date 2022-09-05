def dyphero(cipher_text: str, keys: int):
    alphabet: list[str] = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

    splitted_cipher_text: list[str] = list(cipher_text)

    for letter in splitted_cipher_text:
        if letter != ' ':

            if letter in alphabet:
                index_of_letter: int = alphabet.index(letter) + 1
                plain_text: int = index_of_letter - keys
                print(alphabet[plain_text], end='')

        print(' ')