print()

nome = input("Nome do paciente: ")
peso = float(input("Peso corporal [kg]: "))
alt = float(input("Altura [m]: ").replace(",","."))

print()

# Cálculo do IMC
imc = peso / (alt ** 2)

# Avaliação do IMC calculado
if imc < 18.5:
    aval = "Abaixo do peso"

elif (imc <24.9):
    aval = "Peso normal"

elif (imc <= 29.9):
    aval = "Sobrepeso"

elif (imc <= 34.9):
    aval = "Obesidade grau I"

elif (imc <= 39.9):
    aval = "Obesidade grau II"

elif (imc >= 40):
    aval = "Obesidade grau III (Mórbida)"

# Apresentação final
print(f'                       Nome: {nome}')
print(f'                       Peso: {peso:.2f} kgs' .replace(".",","))
print(f'                     Altura: {alt:.2f} m' .replace(".",","))
print(f'               Valor do IMC: {imc:.2f}' .replace(".",","))
print(f'O paciente se enquadra como: {aval}\n' .replace("." , ","))

# Calcula o peso ideal para corrigir o IMC e se enquadrar em "Peso normal"
pesoIdeal = 24.9 * (alt ** 2)
difPeso = peso - int(pesoIdeal)

# Mensagem para se enquadrar em "Peso normal"

if (imc >= 24.9):
    print(f'O peso ideal para o paciente se enquadrar em \"Peso normal\" seria {f"{pesoIdeal:.2f}".replace("." , ",")} kgs.')
    print(f'Para corrigir o IMC, o paciente precisa reduzir {f"{difPeso:.2f}".replace("." , ",")} kgs.')

if (imc <= 18.5):
    print(f'O peso ideal para o paciente se enquadrar em \"Peso normal\" seria {f"{pesoIdeal:.2f}".replace("." , ",")} kgs.')
    print(f'Para corrigir o IMC, o paciente precisa ganhar {f"{difPeso:.2f}".replace("." , ",")} kgs.')

print()