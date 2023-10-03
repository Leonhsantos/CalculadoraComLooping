# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair
# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 




while True:
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite um valor: "))

    print("Qual operação você deseja fazer ? ")
    print(" 1: Soma")
    print(" 2: Subtração")
    print(" 3: Multiplicação")
    print(" 4: Divisão")
    print(" 0: Sair")

    op = input("Selecione uma opção: ")

    if op == "1":
        print(num1, "+", num2, "=", num1 + num2)
    elif op == "2":
        print(num1, "-", num2, "=", num1 - num2)
    elif op == "3":
        print(num1, "*", num2, "=", num1 * num2)
    elif op == "4":
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            print(num1, "/", num2, "=", num1 / num2)
    elif op == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")

