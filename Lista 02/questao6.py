# 6. Construa um programa que receba um número inteiro positivo informado pelo
# usuário. Caso ele seja par, o programa deve calcular o seu quadrado. Mas, se ele
# for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve imprimir o
# valor calculado.

numero = int(input("Digite um numero:\n"))
quadrado = 0
cubo = 0

if(numero % 2 == 0):
    
    quadrado = numero ** 2
    print(f"O valor e {quadrado}")
else:
    
    cubo = numero ** 3
    print(f"O valor e {cubo}")

