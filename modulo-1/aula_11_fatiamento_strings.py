"""
Referente ao fatiamento de strings, seria básicamente pegar "pedaços" específicos da string por intermédio de seu index.

Por exemplo, temo a frase "It's a burning desire" com 21 caracteres se contarmos também com os espaços entre as palavras. as pasições
sequenciais desssas palavras são os indices que utilizaremos para fatiar as strings, como por exemplo:
"""

frase = "It's a burning desire"

print(frase[1])
#Resulatdo: t

"""
Perceba que ele imprimiu "t" como 1º indice. O motivo para isso é que a contagem de indice em uma string se dá apartir do 0.

Logo, se pedirmos para imprimir 0, receberemos "I" como retorno.
"""

print(frase[0])
#resultado: I

"""
Para fatiarmos essa string, podemos definir o inicio e fim do "pedaço" que iremos pegar, como por exemplo:
"""
print(frase[0:20])
#Resultado: It's a burning desir
print(frase[0:21])
#Resultado: It's a burning desire
"""
Acima, podemos perceber que caso coloque-mos a quantidade exata de caracteres de acordo com o indice, ele não irá exibir tudo,
mas de colocarmos um indice a mais para exibição, o programa exibirá normalmente. Meu chute pessoal é que ele deve aplicar um
Operador lógico como: 

0<20

dessa forma, ele só irá exibir tudo aquilo que for menor que o indice que determinamos, ignorando indices iguais ou maiores que ele.
Por isso, a forma correta de exibir tudo nesse contexto seria:

0<21

Como o indice vai de 0 a 20 caracteres, ele estaria no limite determinado para impressão, uma vez que 20 é < que 21...

Abaixo, podemos aplicar essa lógica sem determinar exatamente um valor inicial ou final, apenas um indice que imprima a partir de algum ponto:
"""

print(frase[:9])#Ele irá imprimir todos os indices menores que 9 
#Resultado: It's a bu

print(frase[9:])#Ele irá imprimir todos os inidices maiorees ou iguais a 9

