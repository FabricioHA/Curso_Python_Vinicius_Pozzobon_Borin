"""
Os inputs no python possibilitam que os usuários insiram valores de entrada customizados para serem armazenados em variáveis,
Possibiliatndo que o programa execulte uma operação baseada na inserção de dados do mesmo:
"""

nome1 = input("Digite o seu nome: ")
tamanho = str(len(nome1))

print("Seu nome tem " + tamanho + " caracteres")

"""
Lembrando que o input por padrão coleta o que o usuário digita como string. Em casos onde precisamos de valores númericos,
podemos converter para float ou int.

Podemos usar funções como: 

float()
int()
str()

elas irão converter o valor para o tipo proposto na função, seja o valor propriamente dito ou uma variavel.
"""
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

idade1 = int(input("Digite a idade de "+nome1+": "))
idade2 = int(input("Digite a idade de "+nome2+": "))

print(f"ao somarmos as idades de {nome1} e {nome2} totalizamos {idade1+idade2} anos")