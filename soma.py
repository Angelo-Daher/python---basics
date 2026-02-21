print("Mini Calculadora")

numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite + para soma, - para subtração ou * para multiplicação: ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    print("Resultado:", numero1 + numero2)
elif operacao == "-":
    print("Resultado:", numero1 - numero2)
elif operacao == '*':
    print('Resultado:', numero1 * numero2)
else:
    print("Operação inválida")