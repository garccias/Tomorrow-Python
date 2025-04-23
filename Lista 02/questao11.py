# 11. Crie um programa no qual o usuário informe 2 números inteiros: a e b. Para que o
# programa continue sua execução, verifique se a < b. Se sim, calcule a soma dos
# números inteiros no intervalo [a, b]. Caso contrário, informe uma mensagem de erro.

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

# Verifica se a < b
if a < b:
    soma = 0
    for i in range(a, b + 1):  
        soma += i
    print(f"A soma dos números no intervalo de {a} até {b} é: {soma}")
else:
    print("Erro: o primeiro número deve ser menor que o segundo.")
