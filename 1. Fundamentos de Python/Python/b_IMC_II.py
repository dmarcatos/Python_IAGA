""" Calcula e interpreta o Índice de Massa Corporal (IMC) """

paciente = input("Nome do paciente: ")
peso = float(input("Peso Corporal [kgs]: "))
altura = float(input("Altura [m]: ").replace(",","."))

imc = peso / (altura ** 2)

print(f"IMC: {imc: .2f}".replace(".",","))

if (imc < 18.5):
    analise = "Abaixo do peso"

else:
    if (imc < 25):
        analise = "Peso Normal"

    else:
        if (imc < 30):
            analise = "Sobrepeso"
        
        else:
            if (imc < 34.9):
                analise = "Obesidade Grau I"
            
            else:
                if (imc < 39.9):
                    analise = "Obesidade Grau II"
                
                else:
                    if (imc >= 40):
                        print ("Obesidade Grau III (Mórbida)")