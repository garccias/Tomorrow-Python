# 4. Escreva um programa que leia 10 notas e informe a média dos alunos.

numero = 0
media = 0 

while(numero < 10):
    
    nota = float(input("Digite a nota:\n"))
    media = media + nota
    numero = numero + 1
    
print(f"A media e {media}")    