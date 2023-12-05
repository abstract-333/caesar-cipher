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


class Gf28:
    def convert(self, number: hex) -> hex:
        shifted_number = int(number, 16) << 1
        print(shifted_number ^ int(number, 16))
        return hex(shifted_number ^ int(number, 16))


print(Gf28().convert("8e"))
