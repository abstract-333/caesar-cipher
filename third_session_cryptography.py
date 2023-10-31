from typing import Final

from first_session_cryptography import CaesarCipher
from second_session_cryptography import Euclidean


class MultiplicativeCipher:
    euclidean = Euclidean()
    LOWER_CASE_ORDER: Final[int] = 97
    UPPER_CASE_ORDER: Final[int] = 65

    def encrypt(self, plain_text: str, key: int) -> None | str:
        if self.euclidean.basic_euclidean(key, 26) != 1:
            return None

        encrypted_text: str = ''
        for char in plain_text:
            order_of_char = ord(char) - self.LOWER_CASE_ORDER
            encrypted_text += chr((order_of_char * key) % 26 + self.UPPER_CASE_ORDER)

        return encrypted_text

    def decrypt(self, encrypted_text: str, key: int) -> None | str:
        if self.euclidean.basic_euclidean(key, 26) != 1:
            return None

        decrypted_text: str = ''
        for char in encrypted_text:
            order_of_char = ord(char) - self.UPPER_CASE_ORDER
            decrypted_text += chr(
                (order_of_char * self.euclidean.extended_euclidean(key, 26)) % 26 + self.LOWER_CASE_ORDER)

        return decrypted_text


class AffineCipher:
    caesar_cipher = CaesarCipher()
    multiplicative_cipher = MultiplicativeCipher()

    def encrypt(self, plain_text: str, key_mult: int, key_add: int) -> str | None:
        encrypted_text_mult = self.multiplicative_cipher.encrypt(plain_text=plain_text, key=key_mult)
        if encrypted_text_mult is not None:
            return self.caesar_cipher.encrypt(encrypted_text_mult, key_add)

        return None

    def decrypt(self, encrypted_text: str, key_mult: int, key_add: int) -> str | None:
        decrypted_text_add = self.caesar_cipher.decrypt(encrypted_text, key_add)
        decrypted_text_mult = self.multiplicative_cipher.decrypt(decrypted_text_add, key_mult)
        if decrypted_text_mult is not None:
            return decrypted_text_mult

        return None


affine_cipher = AffineCipher()
# print(affine_cipher.encrypt("attack", 7, 7))
# print(affine_cipher.decrypt("BEEBPT", 7, 7))
multiplicative_cipher = MultiplicativeCipher()

while True:
    print("To start bruteforce enter 1, or enter 2 to start encryption and decryption")
    choose_type: int = int(input())
    if choose_type == 1:
        print("1- Multiplicative Cipher bruteforce attack")
        print("2- Affine Cipher bruteforce attack")
        choose_type = int(input())
        print("Enter encrypted text to start bruteforce attack")
        text: str = input()
        if choose_type == 1:
            for key_attempt in range(25):
                if Euclidean().basic_euclidean(key_attempt, 26) != 1:
                    continue
                print(multiplicative_cipher.decrypt(encrypted_text=text, key=key_attempt))
        else:
            for key_attempt_add in range(25):
                for key_attempt_mult in range(25):
                    if Euclidean().basic_euclidean(key_attempt_mult, 26) != 1:
                        continue

                    print(affine_cipher.decrypt(text, key_mult=key_attempt_mult, key_add=key_attempt_add))

    else:
        print("Enter text, if you enter it in lowercase I will encrypt the text otherwise I will decrypt it")
        text: str = input()
        print("Enter Key")
        key: int = int(input())
        if text.islower():
            print(multiplicative_cipher.encrypt(plain_text=text, key=key))
        else:
            print(multiplicative_cipher.decrypt(encrypted_text=text, key=key))
