"""
strings nada mais é do que "cadeia de caracteres" em inglês.

cada caractere digitado em uma string é referente a um valor numérico, como por exemplo o modelo ASCII que utiliza padrões decimais, octais e hexadecimais para
representar caracteres em geral.

Como o modelo ASCII tem ficado defasado com o passar dos anos, foi criado um padrão chamado UNICODE, capaz de armazenar mais de 4 bilhões de caracteres
incluindo mandarins e kanjis, por exemplo, ou até mesmo emotes, fora os caracteres originiais do alfabeto como a, b, c, d, etc.
"""

print("Olá, mundo!")

"""
Acima, podemos perceber que cada caractere tem uma posição, um index, para ser mais exato, como por exemplo:

Armazenamento da memória segundo modelo ASCII

String
|   O   |   l   |   a   |   ,   |       |   M   |   u   |   n   |   d   |   o   |   !   |

String representada em ASCII
|   79  |   108 |   97  |   44  |   32  |   109 |   117 |   110 |   100 |   111 |   33  |
"""

'''
python é capaz de armazenar strings em uma só variavel, como por exemplo:
'''

frase = "Olá, mundo!"
print(frase)

"""
Também somos capazes de exibir ou coletar apenas um dos indices da string, como se fosse uma matriz, sendo que o primeiro caractere listado é sempre zero:
"""

print(frase[0])
#Resultado: Irá exibir "O"

print(frase[0+5])
#Resultado: Irá exibir "O" e  "m"

"""
Exemplificando o que aconteceu acima, seria algo como

String
|   O   |   l   |   a   |   ,   |       |   M   |   u   |   n   |   d   |   o   |   !   |

Indice dos caracteres na string (Posição dos caracteres na memória)
|   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |   10  |

ou seja, eu pedi para ele exibir índices específicos da string de acordo com sua posição.
"""