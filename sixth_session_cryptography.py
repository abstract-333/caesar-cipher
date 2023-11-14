# طول المفتاح متغير في خوارزمية RC4
key1 = [1, 2, 3, 6]
p = [1, 2, 2, 2]
key_size1 = 8
result_second_operation = [2, 3, 7, 4, 6, 0, 1, 5]
key_result = [5, 1, 0, 1]


class RC4:
    def __init__(self, key_size: int):
        self.key_size = key_size

    def generateKeyStream(self, key: list[int]) -> list[int]:
        s = []
        temp = []
        key_len: int = len(key)
        for index in range(self.key_size):
            s.append(index)
            temp.append(key[index % key_len])

        j: int = 0
        for index in range(self.key_size):
            j = (j + s[index] + temp[index]) % self.key_size
            s[index], s[j] = s[j], s[index]
        i: int = 0
        j = 0
        result_key = []
        for _ in range(key_len):
            i = (i + 1) % self.key_size
            j = (j + s[i]) % self.key_size
            s[i], s[j] = s[j], s[i]
            result_key.append(s[(s[i] + s[j]) % self.key_size])

        return result_key

    def encrypt(self, plain_text: list[int], key: list[int]) -> list[int]:
        encrypted_text: list[int] = []
        for index in range(len(plain_text)):
            encrypted_text.append(plain_text[index] ^ key[index])

        return encrypted_text


rc4 = RC4(8)
result_key = rc4.generateKeyStream(key1)
print(f"{result_key=}")
result = rc4.encrypt(plain_text=p, key=result_key)
print(f"{result=}")
