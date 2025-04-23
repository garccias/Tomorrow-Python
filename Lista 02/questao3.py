# 3. Escreva um programa para encontrar a soma S = 3 + 6 + 9 + …. + 333.

numero = int(input("Diga um numero:\n"))
salvar = numero

while(numero <= 500):
    
    numero = numero + salvar
    print(f"{numero}")