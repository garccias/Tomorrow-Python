# 7. Construa um programa que solicite ao usuário dois números positivos. Em
# seguida, o programa deve apresentar o seguinte menu:
# 1. Média ponderada, com pesos 2 e 3, respectivamente
# 2. Quadrado da soma dos 2 números
# 3. Cubo do menor número
# Escolha uma opção:
# De acordo com a opção informada, o programa deve calcular a operação
# apresentada no menu. Se a opção escolhida for inválida, o programa deve
# mostrar a mensagem “Opção inválida” e ser encerrado

numero1 = int(input("Digite um numero:\n"))
numero2 = int(input("Digite um numero:\n"))
resultado = 0

menu = int(input("Menu:\n1. Media Ponderada, com pesos 2 e 3\n2. Quadrado da soma dos 2 numeros\n3. Cubo do menor numero"))

if(menu == 1):
    
    resultado = (numero1 * 2 + numero2 * 3) / 2
    print(f"O resultado e {resultado}")
    
elif(menu == 2):
    
    resultado = (numero1 + numero2) ** 2
    print(f"O resultado e {resultado}")


elif(menu == 3):
    if(numero1 > numero2):
        resultado = numero2 ** 3 
        print(f"O resultado e {resultado}")

    else:
        resultado = numero1 ** 3
        print(f"O resultado e {resultado}")

        
else:
    print("Opcão invalida")
    

