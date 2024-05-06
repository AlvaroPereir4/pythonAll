# Calculadora Simples, sem bibliotecas e complicações
# Uso de funções

def soma(a, b):
	print ("\nSoma é: ", a+b)

def subtrai(a, b):
	print ("\nSubtração é: ", a-b)

def multiplica(a, b):
	print ("\nMultiplicação é: ", a*b)

def divide(a, b):
        if (b == 0):
            print("\nNão pode dividir por zero!\n")
        else:
            print("\nO resultado da divisão é: ", a / b, "\n")

print("Calculadora simples, dois valores e então resultado para as 4 operações básicas:")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)