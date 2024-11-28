a= int(input("Digite um numero: "))
b= int(input("Digite um numero: "))

opcao = input("Cauculadora \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nSelecione a operação desejada:")

if opcao ==1:
    soma =a+b
    print(f"Soma de {a} + {b} = {soma}")
elif opcao == 2:
    subtração = a-b
    print(f"Soma de {a} - {b} = {subtração}")
elif opcao==3:
    multiplicação = a*b
    print(f"Soma de {a} X {b} = {multiplicação}")
elif opcao==4:
    divisao = a*b
    print(f"Soma de {a} e {b} = {divisao}")


