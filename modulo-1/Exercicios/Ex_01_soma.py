"""
Desenvolva um algoritmo que solicite ao usuário dois números inteiros. Imprima a soma destes dois números na tela.
"""

while True: #Enquanto o loop for verdadeiro, ele irá continuar a se repitir
    num1 = input("Digite um número inteiro: ")
    num2 = input("Digite outro número inteiro: ")
    # Até aqui, ele executa o que é solicitado

    if not num1.isnumeric() or not num2.isnumeric():
        print("\nErro: Digite um valor válido\n")
        #Nesse ponto, caso o valor digitado não seja numérico, ele emite uma mensagem de erro e retorna ao inicio, solicitando a inserção de dados
    
    else:#Aqui, caso os valores sejam numéricos, ele irá executar as instruções abaixo
        num1 = int(num1)
        num2 = int(num2)
        #acima, ele irá converter os valores em inteiros, uma vez que passaram na condicional acima.
        break #Nesse ponto, ele quebra o loop, tornando-o falso e finalizando o mesmo, já que agora while é falso.

totalSum = num1 + num2

print("\n\nA soma total dos números digitados é de %d" %(totalSum))