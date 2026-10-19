class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

ob1 = Complex(2, 3)
ob2 = Complex(4, 5)
ob3 = ob1 + ob2
print(ob3)