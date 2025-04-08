# 10. Construa um programa que receba do usuário a variação do deslocamento de
# um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o
# programa deve calcular a velocidade média, em m/s, do objeto.

deslocamento = float(input("Digite a variacao do deslocamento em metros:\n"))
tempo = float(input("Digite a variacao do tempo em segundos:\n"))

velocidade = deslocamento / tempo

print(f" a velociade media em m/s é {velocidade}")