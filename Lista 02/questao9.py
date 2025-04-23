# 9. Imagine um sistema de caixa eletrônico. Construa um programa que receba a
# senha de um correntista para validar o seu acesso ao sistema. Considere que a
# senha fictícia do correntista é 123456.
# Considere as seguintes restrições:
# • Quando a senha estiver correta, mostrar a mensagem: “Olá, . Seja bem-vindo ao nosso banco!"
# • Quando o usuário errar a senha pela primeira vez, mostrar a mensagem:
# “Senha incorreta! Você ainda tem 2 tentativas.”
# • Se o usuário errar a senha pela segunda vez, mostrar a mensagem: “Senha
# incorreta! Você ainda tem 1 tentativa.”
# • Se o usuário errar a senha novamente, mostrar a mensagem “Sua senha foi
# bloqueada! Por favor, dirija-se a um de nossos caixas.” e o programa deve ser encerrado.


senha_correta = 123456
tentativas = 3

while tentativas > 0:
    senha = input("Digite sua senha:\n")
    
    if senha == senha_correta:
        print("Olá, correntista. Seja bem-vindo ao nosso banco!")
        break
    else:
        tentativas -= 1
        if tentativas == 2:
            print("Senha incorreta! Você ainda tem 2 tentativas.")
        elif tentativas == 1:
            print("Senha incorreta! Você ainda tem 1 tentativa.")
        elif tentativas == 0:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")