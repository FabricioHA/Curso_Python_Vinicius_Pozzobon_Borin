"""
Em python, executamos o código por quebra de linha. Isso significa que cada instrução
no Python é finalizada apenas após uma quebra de linha, diferente de casos como C,
onde a linguagem termina uma instrução com ";", possibilitando que um programa seja executado em
uma única linha por essa caracteristica.

Também é importante denotar que a execução é de cima para baixo, da esquerda para a direita, padrão em quase
qualquer linguagem de programação.

Abaixo temos um exemplo de instruções em caideia de python:
"""

x = 1
y = 1

z = x + y #z = 1 + 1 = 2
x = x + 2 #x = 1 + 2 = 3
y = y - 1 #y = 1 - 1 = 0

z = x + y #z = 3 + 0 = 3
x = y + 1 #x = 0 + 1 = 1
y = x - 1 #y = 1 - 1 = 0
z = x + y #z = 1 + 0 = 1
print(z) #z = 1