# 12. A força de aceleração é uma energia no espaço-tempo que o Flash utiliza como
# fonte dos seus poderes. Para alcançar a velocidade que deseja, o Flash absorve
# o espaço e o tempo da força de aceleração e a transforma em velocidade. Sua
# tarefa é calcular a velocidade do Flash, dado o espaço e o tempo. Entrada
# A entrada possui dois números inteiros ‘E’ e ‘T’ (1 <= E <= 500) (1 <= T <= 100)
# representando espaço e tempo, respectivamente. Saída
# A saída consiste em uma única linha contendo a velocidade alcançada, sendo a
# velocidade calculada da seguinte forma: V = E/T. Sendo V a nossa velocidade
# desejada e é um número inteiro.

E = int(input("Digite o valor do espaço (E): "))
T = int(input("Digite o valor do tempo (T): "))

if 1 <= E <= 500 and 1 <= T <= 100:
    V = E // T  # cálculo da velocidade com divisão inteira
    print(V)
else:
    print("Erro: os valores devem estar no intervalo 1 <= E <= 500 e 1 <= T <= 100.")
