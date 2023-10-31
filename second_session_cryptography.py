class Euclidean:
    def basic_euclidean(self, a: int, b: int) -> int:
        r1: int = max(a, b)
        r2: int = min(a, b)
        while r2 > 0:
            r: int = r1 % r2
            r1, r2 = r2, r

        return r1

    def extended_euclidean(self, a: int, n: int) -> int | None:
        r1: int = n
        r2: int = a
        t1: int = 0
        t2: int = 1
        while r2 > 0:
            q: int = r1 // r2
            r: int = r1 - (r2 * q)
            r1, r2 = r2, r
            t: int = t1 - (t2 * q)
            t1, t2 = t2, t

        return t1 % n if r1 == 1 else None


euclidean = Euclidean()
# print(euclidean.extended_euclidean(7, 26))
# print(euclidean.basic_euclidean(26, 7))
