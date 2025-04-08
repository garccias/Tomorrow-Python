# 11. Implemente um programa que converta o valor de uma velocidade média em
# km/h para m/s. Para isso, o usuário deve informar o valor da velocidade média.
# Sabe-se que o fator utilizado para essa conversão é 3,6.

velocidadeKm = float(input("Digite a velocidade media em km/h:\n"))
velocidadeMs = velocidadeKm * 3.6

print(f"A velocidade media em m/s é {velocidadeMs}")