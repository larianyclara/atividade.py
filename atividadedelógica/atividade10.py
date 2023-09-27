peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))
imc = peso / (altura**2)

if imc<18.5:
    print("abaixo do peso")
elif 18.5<=imc<30:
    print("peso normal")
elif 25<=imc<30:
    print("acima do peso")
else: 
    print("obeso")