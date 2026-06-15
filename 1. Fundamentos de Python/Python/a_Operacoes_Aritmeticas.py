a = int(input("a: "))
b = int(input("b: "))

soma = a + b
sub = a - b
mult = a * b
divInt = a // b
resto = a % b
divReal = a / b

print(f"Soma: \n {a} + {b} = {soma}")
print(f"Subtração:\n {a} - {b} = {sub}")
print(f"Multiplicação:\n {a} x {b} = {mult}")
print(f"Divisão de Inteiros:\n {a} // {b} = {divInt}")
print(f"Resto da Divisão:\n {a} % {b} = {resto}")
print(f"Divisão de realReal:\n {a} / {b} = {divReal: .3f}")
