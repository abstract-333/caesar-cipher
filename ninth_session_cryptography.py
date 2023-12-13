"""
AES 128 bit:
works with bytes, while DES works with bits
128 bit -> 16 byte -> 4 * 4 matrix
المطلوب كتابة كود shift rows

#########
Write 03 * 48 using Gf(2^8)

(48 * 01) xor (48 * 02)

48 * 01 = 48

48 = 0100 1000
last digit is 0 then, left shift <<
48 * 02 = 10010000

48 xor 90 =
0100 1000 xor 1001 0000 =
1101 1000 = D8

####################################

اوجد ناتج ضرب 03 * 8E ضمن الحقل Gf(2^8)
اكتب تابع برمجي يقوم بإيجاد ناتج ضرب عدد ست عشري ممرر ب 03 ضمن الحقل Gf(2^8) وقم باستدعائه للمثال السابق




"""
import random


class Gf28:
    @classmethod
    def convert(cls, number: hex) -> hex:
        number_integer = int(number, 16)
        shifted_number: int = number_integer << 1

        if number_integer & 128 == 128:
            shifted_number: int = (number_integer - 128) << 1
            shifted_number: int = int("1B", 16) ^ shifted_number

        return hex(shifted_number ^ int(number, 16))


class AES:
    @classmethod
    def shift_elements(cls, items: list[hex], count: int) -> list[hex]:
        for _ in range(count):
            first_element: hex = items.pop(0)
            items.append(first_element)
        return items

    @classmethod
    def shift_rows(cls, state: list[hex]) -> list[hex]:
        result_state: list[hex] = state[:]
        for iteration in range(1, 4):
            result_state[4 * iteration : (4 * iteration) + 4] = cls.shift_elements(
                result_state[4 * iteration : (4 * iteration) + 4], iteration
            )
        return result_state


assert Gf28().convert("48") == "0xd8"
assert Gf28().convert("6E") == "0xb2"
print(Gf28().convert("8E"))
aes = AES()
list_to_shift: list[hex] = [
    "d4",
    "e0",
    "b8",
    "1e",
    "27",
    "bf",
    "b4",
    "41",
    "11",
    "98",
    "5d",
    "52",
    "ae",
    "f1",
    "e5",
    "30",
]
shifted_expected_result: list[hex] = [
    "d4",
    "e0",
    "b8",
    "1e",
    "bf",
    "b4",
    "41",
    "27",
    "5d",
    "52",
    "11",
    "98",
    "30",
    "ae",
    "f1",
    "e5",
]
assert aes.shift_rows(list_to_shift) == shifted_expected_result
