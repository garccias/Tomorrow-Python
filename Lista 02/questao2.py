# 1. Faça um programa que leia 2 notas de um aluno, calcule a média e imprima
# aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6).

nota1 = float(input("Digite a nota 1:\n"))
nota2 = float(input("Digite a nota 2:\n"))

media = (nota1 + nota2) / 2 

if(media >= 6):
    print("Você foi aprovado")
else:
    print("Reprovado")