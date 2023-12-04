"""
بفرض لدينا الصندوق التالي:
i = 1 2 3 4 5 6 7 8 Straight P-box
x = 4 3 2 1 6 7 8 5
1- اوجد خرج الصندوق من اجل الدخل التالي:
1 2 3 4 5 6 7 8
1 0 0 1 0 1 1 1
2- اوجد التبديلة العكسية P^-1
الحل:
1- 10011110

2- P^-1
i = 1 2 3 4 5 6 7 8
x = 4 3 2 1 8 5 6 7
##########################################
بفرض لدينا الصندوق التالي:
 [0, 10, 5, 9]
 [6, 1, 15, 4] Straight P-box
 [2, 11, 14, 7]
 [8, 13, 3, 12]

 1- اوجد خرج الصندوق من اجل التالي:
 1011111000101001
 2- اوجد التبديلة العكسية

 الحل:
 1-
 110101110000011

 2- P^-1
 [0, 5, 8, 14]
 [7, 2, 4, 11]
 [12, 3, 1, 9]
 [15, 13, 10, 6]

##########################
قم بتصميم صندوق مباشر 6*6
ليصبح البت الأول والرابع من الدخل هما البت الخامس والثاني على الترتيب من الخرج
1- اوجد الخرج من أجل: 101100
2- اوجد التبديلة العكسية P^-1
الحل:
i = 1 2 3 4 5 6   Straight P-box
x = 3 4 6 5 1 2

2- P^-1
i = 1 2 3 4 5 6
x = 5 6 1 2 4 3
المطلوب كتابة code الخاص فيه
################################
مطلوب code مبدأ فيستل
"""
from typing import TypeVar


class StraightPBox:
    box: list[int] = []
    inverted_box: list[int] = []
    list_index_starting_from: int = 0

    def __init__(self, box: list[int]):
        self.box = box.copy()
        if 0 not in box:
            self.list_index_starting_from = 1

        inverted_box_list: list[int] = []
        for box_index in range(
            self.list_index_starting_from, len(box) + self.list_index_starting_from
        ):
            inverted_box_list.append(
                box.index(box_index) + self.list_index_starting_from
            )

        self.inverted_box = inverted_box_list.copy()

    def encode(self, list_bin: list[int]) -> list[int]:
        encoded_list: list[int] = []
        for index_counter in range(len(self.box)):
            index_of_digit = self.box[index_counter]
            encoded_list.append(
                list_bin[index_of_digit - self.list_index_starting_from]
            )
        return encoded_list

    def decode(self, list_bin: list[int]) -> list[int]:
        ...


A = TypeVar("A", str, bin)


class Feistel:
    @classmethod
    def xor(cls, left_block: bin, right_block: bin) -> bin:
        if len(left_block) != len(right_block):
            raise ValueError("Right and left blocks must have the same size")

        result_bin: bin = ""

        for index in range(len(left_block)):
            result_bin += format(int(left_block[index]) ^ int(right_block[index]), "b")

        return result_bin

    @classmethod
    def function(cls, variable: bin):
        return variable

    @classmethod
    def encrypt(cls, plain_text: bin) -> bin:
        plain_text_len: int = len(plain_text)

        left_block: bin = plain_text[0 : (plain_text_len >> 1)]
        right_block: bin = plain_text[plain_text_len >> 1 : plain_text_len]

        for iteration in range(16):
            if iteration % 2 == 0:
                left_block = cls.xor(left_block, cls.function(right_block))

            else:
                right_block = cls.xor(cls.function(left_block), right_block)

        return left_block + right_block


print(f"{Feistel().encrypt(plain_text='1011')=}")
print("#" * 100)
test_box = [3, 4, 6, 5, 1, 2]
test_box1 = [0, 2, 3, 1]
box1 = StraightPBox(test_box)
encoded_list = box1.encode([1, 0, 0, 1, 0, 1, 1, 1])
print(f"{encoded_list=}")
print("#" * 100)
print(f"{box1.inverted_box=}")
box2 = StraightPBox(test_box1)
print("#" * 100)
print(f"{box2.inverted_box=}")
