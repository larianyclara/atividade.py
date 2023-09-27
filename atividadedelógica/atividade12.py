nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a terceira nota:"))
ME = float(input("digite a média de exercícios:"))
MA = (nota1 + nota2 * 2 + nota3 * 3 + ME)/7
if MA >=90:
    conceito = "a"
    situação = "aprovado"
elif MA >= 75 and <90:
    conceito = "b"
    situação = "aprovado"
elif MA >=60 and <75:
    conceito = "c"
    situação = "aprovado"
elif MA >=40 and <60:
    conceito = "d"
    situação = "reprovado"
else MA < 40:
    conceito = "e"
    situação = "reprovado"
    
    print("número de alunos")
    print("notas (nota1,nota2,nota3)")
    print("média dos exercícios(ME)")
    print("média de aproveitamento (MA):{ma:.2f}")
    print("conceito:(conceito)")
    print("situação:(situação)")