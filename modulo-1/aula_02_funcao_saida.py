
print("Olá mundo!") #Podemos inclusive utilizar aspas duplas, independente de qual seja, será exibido da mesma maneira.

print((50/2)*3) #O print pode também ser utilizado para fazer impressão de números na tela, além de operações numéricas, como multiplicação, divisão, soma, etc.

print("Olá"+" Mundo!")#Podemos também fazer concatenações no texto de saída, seja utilizando o sinal de mais (+) ou a virgula (,)

print("Olá,","Mundo!")#Não confundir virgula com a virgula dentro do texto, meramente feita para exibição. ela dará um espaço no texto por padrão:
#resultado: Olá, Mundo!   -------- Perceba que não demos um espaço acima no texto. essa é a caracteristica desse elemento no python.

print("O resultado da soma 2+3 é:", 2+3)#Outra caracteristica da concatenação é que com a virgula, podemos fazer calculos de soma sem afetar a concatenação em si
#Se tentarmo executar com a concatenação +, ele irá exibir um erro referente a não ser capaz de somar inteiros com string

print("27", "12", "2001", sep="/")# nesse caso, o código irá executar printando os numeros em texto e, graças a virgula, criar um espaço padrão do concatenador
#com o comando sep="", podemos escolher qual caractere, fora o space, será substituido no separador criado, como acima substituimos por /

