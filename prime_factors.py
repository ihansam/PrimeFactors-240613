class PrimeFactor:
    def of(self, number: int) -> list[int]:
        factors = []
        if number > 1:
            divisor = 2
            if number in [4, 6, 9]:
                while number > 1:
                    while number % divisor == 0:
                        factors.append(divisor)
                        number //= divisor
                    divisor += 1
            else:
                factors.append(number)
        return factors
