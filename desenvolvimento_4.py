def calculadora(num1,num2,operacao):

    if (operacao ==1):
       return num1 + num2
    elif (operacao ==2):
       return num1 - num2
    elif (operacao ==3):
       return num1 * num2
    elif (operador ==4):
       return num1 / num2
    else:
       return 0

executar = true
while executar == true:

    print("qual operação deseja realizar ? :")
    print(" 1-SOMA")
    print(" 2-SUBTRAÇÃO")
    print(" 3-MULTIPLICAÇÃO")
    print(" 4-DIVISÃO")
    oper = int(input())

    if (operacao < 0) or (operacao > 4):
       print("Essa opção não existe!")
    elif (operacao == 0):
       break
     elif (operacao != 0):
        print("Digite um número:")
        num1 = int(input()):
        print("Digite outro numero :")
        num2 = int(input()):

       resultado = calculadora (num,num2,operacao)
       print ("O resultado é:",resultado)