#Tipos de variáveis em Python

"""
Em geral, uma variável pode ser comparada a um dado armazenado em gavetas de um armário (Memória RAM ou Memória do programa),
identificadas por númerações das "gavetas". Para facilitar a localização desses dados, podemos atribuir um nome a essas gavetas,
onde esses nomes se referem a numeração da gaveta que o dado está armazenado.

Gavetas (blocos de espaços) da memória

|   1 idade |   2       |   3       |   4       |
|   5       |   6       |   7       |   8       |
|   9       |   10      |   11 nome |   12      |

Nesse exeplo acima, posso atribuir um nome a um desses espaços na memória como "idade" para localizar precisamente onde o 
valor da variável está alocada
"""

"""
Em python, a linguagem é considerada fracamente tipada, pois ela não requer declaração especíca de tipos como numéricos, texto, ou booleanos,
sendo capaz de detectar qual o tipo de valor que a variável possui.

Linguagens fortemente tipadas são como linguagem C, C++, C# e Java, pois precisamos declarar e especificar o tipo de valor que estamos manipulando. 
"""

"""
Referente ao tipos de Python, temos três tipos primitivos distintos, sendo numérico, caracteres (texto ou string) e literal(Booleano verdadeiro/falso)
"""

#Exemplo

nome = "Alucard"
idade = 1500

print(nome, "Tem", idade, "anos de idade.")

'''
Algumas resalvas sobre variáveis, é que: 

-Não podemos declara-las começando com numeros, ou letras maiusculas ou caracteres especiais. 
-Caracteres espeiciais ou letras com acentos não são permitidos.
-Espaços entre o nome da variavel também não são permitidos.
'''