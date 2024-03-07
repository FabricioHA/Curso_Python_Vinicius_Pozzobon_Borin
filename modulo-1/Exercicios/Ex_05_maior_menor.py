"""
Desenvolva um algoritmo que seja capaz de calcular a soma e a subtração entre 2 valores com vírgula.Crie duas variáveis de teste. 
Uma que testa se a soma é maior do que 10. Outra que testa se a subtração é menor do que 0. Imprima tudo na tela.
"""

print("===== Validar valores maiores ou menores =====\n")

while True:

    num1 = input("Digite o primeiro valor: ")
    num2 = input("Digite o segundo valor: ")

    if not num1.replace(".", "").isnumeric() or not num1.replace(".", "").isnumeric():
        print("\n=== Erro: Valores inválidos. Digite novamente ===\n")
    else:
        num1 = float(num1)
        num2 = float(num2)
        break

sum = num1 + num2
sub = num1 - num2

if sum > 10:
    print("\nO valor %.2f da soma é maior do que 10." %(sum))
else:
    print("\nO valor %.2f da soma é menor do que 10." %(sum))

if sub < 0:
    print("O valor %.2f da subtração é menor que 0.\n" %(sub))
else:
    print("O valor %.2f da subtração é maior que 0.\n" %(sub))