from numbers import Complex
class Numero(Complex):
    pass

# A criação do objeto abaixo vai apresentar o seguinte erro:
# TypeError: Can't instantiate abstract class Numero with abstract 
# methods __abs__, __add__, __complex__, __eq__, __mul__, __neg__, __pos__, 
# __pow__, __radd__, __rmul__, __rpow__, __rtruediv__, __truediv__, conjugate, imag, real
num = Numero()
