from first_session_cryptography import CaesarCipher

########################
p = "heart"
key1 = "red"  # Auto Key
s = "YIDYX"
########################
p2 = "blossom"
key2 = "pink"  # Vigener
s2 = "QTBCHWZ"


class AutoKey:
    caesar_cipher = CaesarCipher()

    def encrypt(self, plain_text: str, key: str):
        encrypted_text: str = ''
        key_length: int = len(key)
        plain_text_length: int = len(plain_text)
        for index in range(plain_text_length):
            key_value: int = 0
            if index > key_length - 1:
                key_value = ord(plain_text[index % key_length]) - self.caesar_cipher.LOWER_CASE_ORDER
            else:
                key_value = ord(key[index]) - self.caesar_cipher.LOWER_CASE_ORDER
            encrypted_text += self.caesar_cipher.encrypt(plain_text=plain_text[index], key=key_value)

        return encrypted_text

    def decrypt(self, encrypted_text: str, key: str):
        plain_text: str = ''
        key_length: int = len(key)
        encrypted_text_length: int = len(encrypted_text)
        for index in range(encrypted_text_length):
            key_value: int = 0
            if index > key_length - 1:
                key_value = ord(plain_text[index % key_length]) - self.caesar_cipher.LOWER_CASE_ORDER
            else:
                key_value = ord(key[index]) - self.caesar_cipher.LOWER_CASE_ORDER
            plain_text += self.caesar_cipher.decrypt(encrypted_text=encrypted_text[index], key=key_value)

        return plain_text


class Vigener:
    caesar_cipher = CaesarCipher()

    def encrypt(self, plain_text: str, key: str):
        encrypted_text: str = ''
        key_length: int = len(key)
        plain_text_length: int = len(plain_text)
        for index in range(plain_text_length):
            key_value: int = 0
            if index > key_length - 1:
                key_value = ord(key[index % key_length]) - self.caesar_cipher.LOWER_CASE_ORDER
            else:
                key_value = ord(key[index]) - self.caesar_cipher.LOWER_CASE_ORDER
            encrypted_text += self.caesar_cipher.encrypt(plain_text=plain_text[index], key=key_value)

        return encrypted_text

    def decrypt(self, encrypted_text: str, key: str):
        plain_text: str = ''
        key_length: int = len(key)
        encrypted_text_length: int = len(encrypted_text)
        for index in range(encrypted_text_length):
            key_value: int = 0
            if index > key_length - 1:
                key_value = ord(key[index % key_length]) - self.caesar_cipher.LOWER_CASE_ORDER
            else:
                key_value = ord(key[index]) - self.caesar_cipher.LOWER_CASE_ORDER
            plain_text += self.caesar_cipher.decrypt(encrypted_text=encrypted_text[index], key=key_value)

        return plain_text


auto_key = AutoKey()
vigener = Vigener()
print(auto_key.encrypt(plain_text=p, key=key1))
print(auto_key.encrypt(plain_text=s, key=key1))
print(vigener.encrypt(plain_text=p2, key=key2))
print(vigener.decrypt(encrypted_text=s2, key=key2))
