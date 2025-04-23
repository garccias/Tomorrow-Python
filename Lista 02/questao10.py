# 10. Crie um programa no qual o usuário informe a idade de um número
# indeterminado de alunos. Para encerrar a leitura dos dados, o usuário deve
# informar uma idade negativa.

print("Digite a idade dos alunos. Para encerrar, digite uma idade negativa.")

while True:
    idade = int(input("Idade do aluno: "))
    
    if idade < 0:
        print("Encerrando o programa...")
        break
    else:
        print(f"Idade registrada: {idade}")
