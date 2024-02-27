"""
Variavieis do tipo booleano são variaveis lógicas que possuem apenas dois tipos distintos de valores: true (Verdadeiro) or false (falso)

Podemos usar operadores lógicos como:

==  Igual
<   menor
>   maior
<=  menor ou igual
>=  maior ou igual
!=  Diferente
"""

#exemplos

a=1#recebe 1
b=5#recebe 5

#resposta recebe o resultado da comparação lógica (true/false)
resposta = a==b
print("a é menor do que b? Resposta:", resposta)

resposta = a!=b
print("a é diferente de b? Resposta:", resposta)

#Exercicio
'''
Crie uma variável que receba uma nota de um aluno. Crie outra variável que receba o resultado de uma comparação lógica entre a nota escolhida e o valor 7, que é a média para aprovação. Caso a nota seja maior ou igual a 7, o resultado deve ser verdadeiro. Imprima o resultado da comparação na tela.
'''
aluno = "Jubileu"
nota = 6.0

print("\n\nResultado da nota geral\n")
if nota <= 6.0 and nota>= 0.0:
    print(aluno+"... REEEEPROVADO!!!")
elif nota<=10.0 and nota >=7.0:
    print(aluno+"... TÁ APROVADISSIMO MULEQUE!!")
else:
    print("Valor digitado é inválido\nFavor, digitar novamente")

'''
Obs: O equivalente de && e || em python é and e or 
'''