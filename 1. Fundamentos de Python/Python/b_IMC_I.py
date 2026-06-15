""" Calcula e interpreta o Índice de Massa Corporal (IMC) """

nome = input("Nome do Paciente: ")
peso = int(input("Peso do Paciente [kg]: "))
altura = float(input("Altura do Paciente [m]: ").replace(",","."))

imc = peso / (altura ** 2)

print(f"Imc = {imc: .2f}")

if imc < 18.5:
    print("Abaixo do peso")

if (imc >= 18.5 and imc <24.9):
    print("Peso normal")

if (imc >= 25 and imc <= 29.9):
    print("Sobrepeso")

if (imc >= 30 and imc <= 34.9):
    print("Obesidade grau I")

if (imc >= 35 and imc <= 39.9):
    print("Obesidade grau II")

if (imc >= 40):
    print("Obesidade grau III (Mórbida)")


