# 13. Construa um programa que ler os componentes de um endereço, rua, número,
# complemento e cep, um em cada linha, e imprimir o endereço no seguinte
# formato: Rua {rua}, n. {número}, {complemento} - {cep}

rua = str(input("Digite sua rua:\n"))
numero = int(input("Digite o numero:\n"))
complemento = str(input("Digite o complemento:\n"))
cep = int(input("Digite o cep:\n"))

print(f"Rua {rua}, n. {numero}, {complemento} - {cep}")
