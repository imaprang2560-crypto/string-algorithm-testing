def caesar_cipher(s, k):

    result = ""

    k = k % 26

    for char in s:

        if char.islower():

            result += chr((ord(char) - 97 + k) % 26 + 97)

        elif char.isupper():

            result += chr((ord(char) - 65 + k) % 26 + 65)

        else:

            result += char

    return result