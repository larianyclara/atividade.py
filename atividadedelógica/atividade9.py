altura = float(input("Digite a altura:"))
sexo = input("Digite o sexo ( M para Masculino e F para Feminino): ")
if sexo == "M":
        peso = (72.7 * altura) - 58
        print ("O peso ideal é: ", peso)
elif sexo == "F":
        peso = (62.1 * altura) - 44.7
        print ("O peso ideal é: ", peso)