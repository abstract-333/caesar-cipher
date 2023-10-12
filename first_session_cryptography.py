import string
from typing import Final


class CaesarCipher:
    LOWER_CASE_ORDER: Final[int] = 97
    UPPER_CASE_ORDER: Final[int] = 65

    def encrypt(self, plain_text: str, key: str | int) -> str:
        encrypted_text = ""

        key_order = ord(key.lower()) - self.LOWER_CASE_ORDER
        for i in range(len(plain_text)):
            char_from_text = plain_text[i]
            order_of_char = ord(char_from_text) - self.LOWER_CASE_ORDER
            encrypted_text += chr((order_of_char + key_order) % 26 + self.UPPER_CASE_ORDER)

        return encrypted_text

    def decrypt(self, encrypted_text: str, key: str | int) -> str:
        decrypted_text = ""

        key_order = ord(key.upper()) - self.UPPER_CASE_ORDER
        for i in range(len(encrypted_text)):
            char_from_text = encrypted_text[i]
            order_of_char = ord(char_from_text) - self.UPPER_CASE_ORDER
            decrypted_text += chr((order_of_char - key_order) % 26 + self.LOWER_CASE_ORDER)

        return decrypted_text


print(CaesarCipher().encrypt(plain_text="security", key='a'))
print(CaesarCipher().decrypt(encrypted_text="HTRJGXIN", key='p'))

# Bruteforce attack
for char in string.ascii_letters:
    print(CaesarCipher().decrypt(encrypted_text="HTRJGXIN", key=char))
