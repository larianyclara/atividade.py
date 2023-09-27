salário = float(input("digite o salário"))
if salário <= 1999:
    print("salário-0")
elif salário <=2000:
    print("salário-7,5%")
elif salário <=3500:
    print("salário-15%")
elif salário <=3900:
    print("salário-22,5%")
elif salário <=4670:
    print("salário - 27,5%")
else:
    print("recebe mais que 4670")