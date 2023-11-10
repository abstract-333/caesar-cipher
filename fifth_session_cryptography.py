from math import ceil

p = "doll"
k = "moon"  # PlayFair
r = "IDKYPY"
###########
p2 = "dreams"
k2 = "hallowen"  # ADFGVX
k3 = "night"
r2 = "GDAAFAGADDXGAGA"

import numpy as np


# معالجة النص الأصلي في Playfair
# التشفير باستخدام ADFGVX
class PlayFair:
    def removeRepeatedCharacters(self, text: str) -> str:
        nonduplicated: str = ""
        for char in text:
            if nonduplicated.count(char) == 0:
                nonduplicated += char
        return nonduplicated

    def constructKeyMatrix(self, key: str):
        nonduplicated: str = self.removeRepeatedCharacters(key)
        alphabet: list = list("abcdefghiklmnopqrstuvwxyz")
        key_matrix = [[0 for num in range(5)] for num1 in range(5)]
        key_len = len(nonduplicated)
        for index in range(key_len):
            char = nonduplicated[index]
            key_matrix[index // 5][index % 5] = char
            alphabet.remove(char)
        alphabet_len: int = len(alphabet)
        for index in range(alphabet_len):
            char = alphabet[index]
            key_matrix[(index + key_len) // 5][(index + key_len) % 5] = char
        return key_matrix

    def getPairsOfCharacters(self, text: str) -> list[str]:
        pair_chars: list[str] = []
        for index_chars in range(0, len(text), 2):
            pair_chars.append(text[index_chars] + text[index_chars + 1])

        return pair_chars

    def handlingPlainText(self, plain_text: str) -> list[str]:
        plain_text: str = plain_text.replace(" ", "")
        index_char = 0
        while index_char < len(plain_text) - 1:
            first_char = plain_text[index_char]
            second_char = plain_text[index_char + 1]
            if first_char == second_char:
                plain_text = (
                    plain_text[: index_char + 1] + "x" + plain_text[index_char + 1 :]
                )
            index_char += 2

        if len(plain_text) % 2 != 0:
            plain_text += "z"

        return self.getPairsOfCharacters(plain_text)


class ADFGVX:
    ADFGVX = "ADFGVX"

    def removeRepeatedCharacters(self, text: str) -> str:
        nonduplicated: str = ""
        for char in text:
            if nonduplicated.count(char) == 0:
                nonduplicated += char
        return nonduplicated

    def constructKeyMartix(self, key: str) -> str:
        key_matrix = ""
        key_matrix += self.removeRepeatedCharacters(key).upper()
        alphabet_with_nums: list = list("abcdefghijklmnopqrstuvwxyz123456789".upper())
        key_len: int = len(key)
        alphabet_len: int = len(alphabet_with_nums)
        for char in alphabet_with_nums:
            if char in key_matrix:
                continue
            key_matrix += char
        return key_matrix

    def encrypt(self, plain_text: str, first_key: str, second_key: str):
        key_matrix = self.constructKeyMartix(key=first_key)
        plain_text = plain_text.replace(" ", "").upper()
        cipher_text = ""
        for char in plain_text:
            index_key_matrix = key_matrix.find(char)
            cipher_text += (
                self.ADFGVX[index_key_matrix // 6] + self.ADFGVX[index_key_matrix % 6]
            )
        cipher_text_len = len(cipher_text)
        column_size = ceil(cipher_text_len / len(second_key))
        count_added_chars = (len(second_key) * column_size) - cipher_text_len
        cipher_text_shuffled = ""
        cipher_text += "A" * count_added_chars
        sorted_key = "".join(sorted(second_key))
        for char in sorted_key:
            temp_text = ""
            index = second_key.find(char)
            for inner_index in range(column_size):
                temp_text += cipher_text[index + (inner_index * len(second_key))]
            cipher_text_shuffled += temp_text

        return cipher_text_shuffled


play_fair = PlayFair()
adfgvx = ADFGVX()
key_matrix = play_fair.constructKeyMatrix("moon")
filtered_text = play_fair.handlingPlainText("some sasy")
result = adfgvx.encrypt(p2, k2, k3) == r2
# result = adfgvx.encrypt("COMPUTER", "orange", "rinad")
# result = adfgvx.constructKeyMartix("orange")
print(f"{filtered_text=}")
print(f"{key_matrix=}")
print(f"{result=}")
