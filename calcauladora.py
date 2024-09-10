def soma(x, y):
    return "O resultado da soma é igual a " + str(x + y)

def subtracao(x, y):
    return "O resultado da subtração é igual a " + str(x - y)

def multiplicacao(x, y):
    return "O resultado da multiplicação é igual a " + str(x * y)

def divisao(x, y):
    if y == 0:
        return "Divisão por 0 ERROR"
    else:
        return "O resultado da divisão é igual a " + str(x / y)

# INICIANDO CALCULADORA
print("=======================")
print("======CALCULADORA======")
print("=======================")

flag = 1
while flag == 1:
    valor1 = float(input("Informe o primeiro valor: "))
    
    print("======OPERAÇÕES======")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    
    operacao = int(input("Informe a operação: "))
    while operacao < 1 or operacao > 4:
        operacao = int(input("Informe a operação válida: "))  # Corrigido para converter a operação em int
        
    valor2 = float(input("Informe o segundo valor: "))
    
    if operacao == 1:
        print(soma(valor1, valor2))
    elif operacao == 2:
        print(subtracao(valor1, valor2))
    elif operacao == 3:
        print(multiplicacao(valor1, valor2))
    elif operacao == 4:
        print(divisao(valor1, valor2))
    
    flag = int(input("Deseja fazer outra operação? Digite 1 para sim e 0 para não: "))
    if(flag != 1):
        print("Obrigado por utilizar os nossos serviços, até a próxima!!!")