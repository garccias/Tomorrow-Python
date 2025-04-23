# 5. Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número.

numero = int(input("Digite um numero:\n"))
contador = 1
resultado = 0

while(contador < 10):
    
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")    
    contador = contador + 1