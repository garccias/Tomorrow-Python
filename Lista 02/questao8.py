# 8. Um professor de Matemática deseja construir um programa para gerar uma
# Progressão Aritmética (PA). Para isso, devem ser informados 3 argumentos: a)
# primeiro termo, b) quantidade de termos e c) razão.


primeiro = int(input("Digite o primeiro termo:\n"))
quantidade = int(input("Digite a quantidade de termos:\n"))
razao = int(input("Digite a razao:\n"))
termo = 0

for i in range(quantidade):
    termo = primeiro + i * razao
    print(termo)