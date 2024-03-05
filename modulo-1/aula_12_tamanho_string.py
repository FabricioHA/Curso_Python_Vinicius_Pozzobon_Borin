"""
Em python, podemos saber a quantidade total de caracteres atravéz de uma função chamada
len(), significando Length (Comprimento).

Em termos gerais, ela consegue coletar quantos caracteres totais temos na string, imprimindo o "comprimento" total da mesma,
como por exemplo:
"""

nome = "Fabrício Holandino da Silva"
tamanho = len(nome)
print(tamanho)
#Resultado: 27

"""
Sua contagem acontece apartir do 1, exibindo exatamente quantos caracteres se encontram na string, não suas posições
específicas.

Também podemos trabalhar com valores booleanos apartir da quantidade de caracteres utilizando operadores lógicos, como
por exemplo:
"""

tamanho = len(nome) <=15
print(tamanho)
#Resultado: False


"""
Resultado emitido como falso pois a largura contada como 27 é > do que 15, tornando essa operação falsa.
"""