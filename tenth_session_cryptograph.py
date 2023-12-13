class Knapsack:
    @staticmethod
    def generate_public_key(
        private_key: list[int], max_value: int, base: int
    ) -> list[int]:
        public_key: list[int] = [
            (base * element) % max_value for element in private_key
        ]
        return public_key

    @staticmethod
    def encrypt(plaintext_bin: bin, public_key: list[int]) -> int:
        encrypted_message: int = sum(
            public_key[i] for i in range(len(plaintext_bin)) if plaintext_bin[i] == "1"
        )

        return encrypted_message

    @staticmethod
    def decrypt(
        ciphertext: int, private_key: list[int], max_value: int, base: int
    ) -> bin:
        r_inverse: int = pow(base, -1, max_value)
        decrypted_message: bin = ""
        number_ciphered = (ciphertext * r_inverse) % max_value
        for element in reversed(private_key):
            if number_ciphered >= element:
                decrypted_message = "1" + decrypted_message
                number_ciphered -= element
            else:
                decrypted_message = "0" + decrypted_message

        return decrypted_message


if __name__ == "__main__":
    base: int = 31
    max_value: int = 105
    plaintext1 = "011000"
    plaintext2 = "101110"
    plaintext3 = "110101"
    public_key = [62, 93, 81, 88, 102, 37]
    private_key = [2, 3, 6, 13, 27, 52]
    generated_public_key: list[int] = Knapsack.generate_public_key(
        private_key=private_key, max_value=max_value, base=base
    )
    assert generated_public_key == public_key
    ciphertext1 = Knapsack.encrypt(plaintext1, public_key)
    ciphertext2 = Knapsack.encrypt(plaintext2, public_key)
    ciphertext3 = Knapsack.encrypt(plaintext3, public_key)
    assert ciphertext1 == 174
    assert ciphertext2 == 333
    assert ciphertext3 == 280
    decrypted_plaintext1 = Knapsack.decrypt(
        ciphertext=ciphertext1, private_key=private_key, base=base, max_value=max_value
    )
    decrypted_plaintext2 = Knapsack.decrypt(
        ciphertext2, private_key, base=base, max_value=max_value
    )
    decrypted_plaintext3 = Knapsack.decrypt(
        ciphertext3, private_key, base=base, max_value=max_value
    )
    assert decrypted_plaintext1 == plaintext1
    assert decrypted_plaintext2 == plaintext2
    assert decrypted_plaintext3 == plaintext3

    print("--ALL Done--")
    print("#" * 30)
