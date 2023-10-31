import string
from typing import Final


class CaesarCipher:
    LOWER_CASE_ORDER: Final[int] = 97
    UPPER_CASE_ORDER: Final[int] = 65

    def encrypt(self, plain_text: str, key: int) -> str:
        encrypted_text = ""

        for i in range(len(plain_text)):
            char_from_text = plain_text[i]
            order_of_char = ord(char_from_text) - self.LOWER_CASE_ORDER
            encrypted_text += chr((order_of_char + key) % 26 + self.UPPER_CASE_ORDER)

        return encrypted_text

    def decrypt(self, encrypted_text: str, key: int) -> str:
        decrypted_text = ""

        for i in range(len(encrypted_text)):
            char_from_text = encrypted_text[i]
            order_of_char = ord(char_from_text) - self.UPPER_CASE_ORDER
            decrypted_text += chr((order_of_char - key) % 26 + self.LOWER_CASE_ORDER)

        return decrypted_text


# caesar_cipher: CaesarCipher = CaesarCipher()
# print(caesar_cipher.encrypt(plain_text="security", key='a'))
# print(caesar_cipher.decrypt(encrypted_text="HTRJGXIN", key='p'))
#
# # Bruteforce attack
# for char in string.ascii_lowercase:
#     print(caesar_cipher.decrypt(encrypted_text="HTRJGXIN", key=char), "", char)
