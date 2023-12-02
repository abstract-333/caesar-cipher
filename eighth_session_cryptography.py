"""
DES:
feistel
تعمل على مستوى البتات
block_size: 64 bits
key_size: 64 bits, 56 bits
subkey_sizes: 48 bits
rounds: 16
sub_keys: 16
1 2 9 16 -> one bit
others -> 2bits
المطلوب توليد المفاتيح الفرعية

############################################

Triple DES uses two keys, each key = 64 bits
DES_encryption(k1) -> DES_decryption(k2) -> DES_encryption(k1)

#########################################################

Rijindael:
لا تستخدم مبدأ فيستل
Rijindael 128 bits && block_size = 128 bits && iterations = 10 && num_keys = 10
Rijindael 192 bits && block_size = 192 bits && iterations = 12 && num_keys = 12
Rijindael 256 bits && block_size = 256 bits && iterations = 14 && num_keys = 14
"""
from typing import Final


class DES:
    PC1: Final[list[int]] = [
        57,
        49,
        41,
        33,
        25,
        17,
        9,
        1,
        58,
        50,
        42,
        34,
        26,
        18,
        10,
        2,
        59,
        51,
        43,
        35,
        27,
        19,
        11,
        3,
        60,
        52,
        44,
        36,
        63,
        55,
        47,
        39,
        31,
        23,
        15,
        7,
        62,
        54,
        46,
        38,
        30,
        22,
        14,
        6,
        61,
        53,
        45,
        37,
        29,
        21,
        13,
        5,
        28,
        20,
        12,
        4,
    ]
    PC2: Final[list[int]] = [
        14,
        17,
        11,
        24,
        1,
        5,
        3,
        28,
        15,
        6,
        21,
        10,
        23,
        19,
        12,
        4,
        26,
        8,
        16,
        7,
        27,
        20,
        13,
        2,
        41,
        52,
        31,
        37,
        47,
        55,
        30,
        40,
        51,
        45,
        33,
        48,
        44,
        49,
        39,
        56,
        34,
        53,
        46,
        42,
        50,
        36,
        29,
        32,
    ]

    def left_shift(self, text: bin, index: int) -> bin:
        text_shifted: bin = ""
        start_index = 2
        if index in (1, 2, 9, 16):
            start_index = 1

        text_length: int = len(text)
        for iteration_index in range(start_index, text_length):
            text_shifted += text[iteration_index]

        for iteration_index in range(0, start_index):
            text_shifted += text[iteration_index]

        return text_shifted

    def generate_subkeys(self, key: str) -> list[hex]:
        key_binary = format((int(key, 16)), "064b")
        key_permuted: bin = "".join([key_binary[i - 1] for i in self.PC1])
        left: bin = key_permuted[:28]
        right: bin = key_permuted[28:]

        subkeys: list[bin] = []
        for round_number in range(1, 17):
            left = self.left_shift(left, index=round_number)
            right = self.left_shift(right, index=round_number)
            shifted_text: bin = left + right
            permuted_text: bin = "".join([shifted_text[i - 1] for i in self.PC2])
            subkey: hex = format(int(permuted_text[:], 2), "x")
            subkeys.append(subkey.upper())

        return subkeys


# print(f"{DES().left_shift('1100', 8)=}")
# print(f"{DES().left_shift('1100', 2)=}")
print(f"{DES().generate_subkeys('AABB09182736CCDD')=}")
