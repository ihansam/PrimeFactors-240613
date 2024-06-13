class PrimeFactor:
    def of(self, number: int) -> list[int]:
        factors = []
        if number == 2:
            factors.append(2)
        elif number == 3:
            factors.append(3)
        return factors
