etiqueta = float(input("digite o preço normal de etiqueta:"))
condição = int(input("digite a escolha de condição de pagamento(1 para á vista em dinheiro ou cheque e recebe 10% de desconto, 2 para á vista no cartão de crédito e recebe 15% de desconto, 3  em duas vezes, preço normal de etiqueta sem juros, 4 em duas vezes, preço normal de etiqueta mais juros de 10%: "))
if condição == 1:
    pago =  etiqueta - ( etiqueta ** 0.10)
elif condição == 2:
       pago =  etiqueta - ( etiqueta ** 0.15)
elif condição == 3:
            pago = etiqueta / 2
elif condição  == 4:
            pago = ( etiqueta / 2) + ((etiqueta / 2) ** 0.10)
            print(" o valor será p preço normal de etiqueta")