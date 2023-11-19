# طول المفتاح متغير في خوارزمية RC4
import math

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


class RC4Analyzing:
    @classmethod
    def convert_bin(cls, list_numbers: list[int]) -> str:
        numbers_binary: bin = ""
        for number in list_numbers:
            binary_value = format(number, "03b")
            numbers_binary += binary_value
        return numbers_binary

    def change_point_test(self, list_numbers: list[int]) -> (int, float):
        numbers_binary: bin = self.convert_bin(list_numbers)
        print(numbers_binary)
        max_value: float = 0
        len_binary: int = len(numbers_binary)
        count_ones_in_binary = numbers_binary.count("1")
        for index_bin in range(1, len_binary):
            max_value = max(
                max_value,
                abs(
                    len_binary * numbers_binary[: index_bin + 1].count("1")
                    - index_bin * count_ones_in_binary
                ),
            )
        coefficient: float = (-2 * max_value**2) / (
            len_binary * count_ones_in_binary * (len_binary - count_ones_in_binary)
        )

        return max_value, math.exp(coefficient)

    def binary_derivative_test(self, list_numbers: list[int]):
        numbers_binary: bin = self.convert_bin(list_numbers)
        print(numbers_binary)
        len_binary: int = len(numbers_binary)
        binary_derived: bin = numbers_binary
        for index in range(len_binary - 1):
            temp_binary: bin = ""
            for binary_index in range(1, len(binary_derived)):
                temp_binary += bin(
                    int(binary_derived[binary_index], 2)
                    ^ int(binary_derived[binary_index - 1], 2)
                )[2:]
            binary_derived = temp_binary
            print(f"{temp_binary=}, {index=}")
            print(temp_binary.count("1") / (len_binary - index))
            print("*" * 20)


rc4 = RC4(8)
result_key = rc4.generateKeyStream(key1)
print(f"{result_key=}")
RC4_result = rc4.encrypt(plain_text=p, key=result_key)
print(f"{RC4_result=}")
change_point = RC4Analyzing().change_point_test(RC4_result)
binary_derivative_test = RC4Analyzing().binary_derivative_test(RC4_result)
print(f"{change_point=}")
result = rc4.encrypt(plain_text=p, key=RC4_result)
print(f"{result=}")
