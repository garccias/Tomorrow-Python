# 12. Imagine a situação em que existem 2 copos com sucos de fruta. O primeiro copo
# está com suco de laranja, enquanto o segundo está com suco de acerola. Você
# deseja mudar os sucos de copo, isto é, colocar o suco de laranja no segundo
# copo e o suco de acerola no primeiro copo. No entanto, não é desejável que eles
# se misturem. Agora, vamos transformar esta situação em um programa. Nas
# duas linhas abaixo, nós colocamos o suco de laranja no copo1 e o suco de
# acerola no copo2:
# copo1 = “laranja”
# copo2 = “acerola”

# Continue o programa de modo a transferir o suco de acerola para o copo1 e o
# suco de laranja para o copo2. Ao fim, imprima as variáveis suco1 e suco2.

copo1 = "laranja"
copo2 = "acerola"

temporario = copo1
copo1 = copo2
copo2 = temporario

print(f"O copo 1 é {copo1} e o copo 2 {copo2}")