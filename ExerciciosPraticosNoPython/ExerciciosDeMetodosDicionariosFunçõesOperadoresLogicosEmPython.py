

# Exemplos de uso dos métodos:

#criando uma lista de 1 a 20 com o append:

x = []

for i in range(1, 21):
  x.append(i)
  print(i)

# forma para localizar um elemento dentro de uma lista e remove-lo

x = [1,2,3,4,5,6,7,8,9]

print('valor contido na variável X: ', x, '\n')

y = int(input('digite um numero para apagar da lista: \n'))

if y in x:
  x.remove(y)
  print('O valor foi removido com sucesso\n')

print('lista atualizada:', x, '\n')

# Lista de Lista

x = [['ruan', 28], ['carlos', 26], ['samuel', 1]]

print('valor da lista na posição 0: ', x[0], '\n') # digitar dentro dos colchetes o valor que corresponde a posição desejada, e imprime a lista que está contida nessa posição.

print('valor contido na posição 0 da lista pricipal e valor contido da lista interna na posição 0: ', x[0][0], '\n')

print('valor contido na posição 2 da lista pricipal e valor contido da lista interna na posição 0: ', x[2][0], '\n')




#Extrutura de dados: dicionário

x = {'ruan': 28}

print('valor da variável x utilizando o {chave: valor}: ', x['ruan'], '\n')

y = dict(ruan = 28)

print('valor da variável y utilizando o direct(chave = valor): ', y['ruan'], '\n')

#OBS: Sempre para consulta deve-se utilizar a chave para imprimir o valor, ao contrario não funciona.

personagens = {'metal gear solid 1': 'Solid Snake', 'metal gear solid 2': 'Riden', 'metal gear solid 3': 'bigboss', 'metal gear solid 4': 'Solid/Old Snake', 'metal gear solid 5': 'bigboss'}

print('conteúdo da lista personagens: ', personagens, '\n')

print('consulta do valor pela chave metal gear solid 3: ', personagens['metal gear solid 3'], '\n')

#utilizando o método len para contar quantos valores tem dentro do dicionário:

print('quantidade de valores dentro do dicionário personagens: ', len(personagens), '\n') #observe que o
#len contou somente os valores contidos dentro do dicionário e não a quantidade de chaves.

#Utilizando o método pop para remover uma chave/valor:

personagens.pop('metal gear solid 2')

print('dicionário personagens, após o método pop: ', personagens, '\n')

#criando um dicionário dentro de uma lista:

jogos = [{'titulo': 'The Last of Us', 'genero': 'sobrevivencia', 'ano de lançamento': 2013}, {'tituilo': 'resident evil 8', 'genero': 'terror', 'ano de lançamento': 2021}, {'titulo': 'Horizon Forbidden West', 'genero': 'aventura', 'ano de lançamento': 2022}]

print('dentro da lista jogos, seleciona o dicionário na posição 1: ', jogos[1], '\n')

print('dentro da lista jogos, seleciona o dicionário na posição 2, chave titulo e chave ano de lançamento: ', jogos[2]['titulo'], jogos[2]['ano de lançamento'])


#criação de funções

'''
uma função serve para optimizar o código uma vez que criada será necessário
somente chamar a função e atribuir parâmetros a ela.

método: def minhafunção()

'''

#definindo uma função:

def mensagemDeErro():
  print('a função foi definina para imprimir estás mensagens de erro: ')
  print('o comando digitado é inválido')
  print('programa encerrado\n')

#chamando a função:

mensagemDeErro()

#definindo uma função:

def MediaAritmetica(n1, n2):
  print(f'a média é: {((n1+n2)/2)}')

#chamando a função:

MediaAritmetica(7, 10) #aqui o preenchimento das variáveis n1 e n2 são feitas na ordem prédefinina na função.

MediaAritmetica(n2 = 5, n1 = 7) # chamando a variável dentro da função é possivel escolher a onde de preenchimento.

#combinando funções:

def somaDosNum(*list): # aqui utilizou-se o ponteiro * para indicar que a variável será uma lista.
  print('a soma dos numeros é:', sum(list),'\n') #combinando a função sum() ira criar uma lista indeterminada de valores com numeros e somará todos eles.

somaDosNum(int(input('insira o numero para somar: ')),
           int(input('insira o numero para somar: ')),
           int(input('insira o numero para somar: ')))

#utilizando o return em uma função

def retorna():
  return 100

z = retorna() # foi atribuido a variável z o valor de 100, uma vez que o comando return ejeta o valor para dentro de uma variável.

print('valor de return atribuído a z:', z, '\n')

def retorna2(n1, n2, n3, n4, p1, p2, p3, p4):
  return ((n1*p1 + n2*p2 + n3*p3 + n4*p4) / (p1 + p2 + p3 + p4) ) # aqui foi atribuido ao return uma formula matemática de média ponderada.

result = retorna2(
          float(input('nota 1: ')),
          float(input('nota 2: ')),
          float(input('nota 3: ')),
          float(input('nota 4: ')),
          int(input('peso 1: ')),
          int(input('peso 2: ')),
          int(input('peso 3: ')),
          int(input('peso 4: ')))

print('sua nota é: ', result, '\n')

def tupla(): # tuplas são valores fixos atribuidos a variáveis.
  return(3.14, 9.6)

a, b = tupla()

print(f'valor de Pi: {a}\n',f'valor da gravidade em Niltons: {b}')





'''
Um módulo é um conjunto de funções que ajuda o programador a agilizar o processo de
programação uma vez que todas as funções que serão utilizadas em seu programa pode ser
criadas previamente e separadas do corpo do programa central, enchugando o o código.

aqui nessa seção faremos a importação de um modulo feito anteriormente e importado para dentro do nosso programa.
'''

from google.colab import drive # comando para realizar a montagem do google drive para importar arquivos e modulos para dentro do programa
drive.mount('/content/drive')




#Aqui realizamos o import do caminho até a pasta onde o arquivo modulos.py se encontra

import sys
sys.path.insert(0,'/content/drive/MyDrive/COLAB ESTUDOS/funções/')



# Aqui realizamos a importação do modulo em sí para dentro do programa e o renomeamos como op

import modulos as op

print(op.retorna2(8,9,7,10,2,3,1,2)) # para chamar uma função dentro de um módulo externo é preciso colocar o nome do arquivo um ponto e o nome da função contida dentro do arquivo

print(op.tupla())

print(op.retorna())

op.somaDosNum(2, 4 , 6 ,8)

op.MediaAritmetica(7,8)



#Criando e manipulando aquivos

arquivo = open('estudo de python.txt', 'w') # cria um arquivo .txt e sobrescreve todo seu conteúdo.

texto = '''
testando se está funcionando.
'''

arquivo.write(texto) # insere dentro do conteúdo da variável texto dentro do arquivo .txt




arquivo = open('estudo de python.txt', 'a') # abre o arquivo e altera seu conteúdo

texto = '''
agora estou adicionando esta frase no arquivo.
'''

arquivo.write(texto) # insere dentro do conteúdo da variável texto dentro do arquivo .txt




# Uma forma de lê o conteúdo de um arquivo .txt dentro do prompt

arquivo = open('estudo de python.txt', 'r') # abre e lê o conteúdo do arquivo .txt

texto = arquivo.read() #armazena em uma variável o contúdo do arquivo .txt

print('conteúdo do arquivo .txt: ', texto)

#abaixo leremos o conteúdo do arquivo .txt e em seguida criaremos uma lista.

arquivo = open('estudo de python.txt', 'r')

listadelinhas = arquivo.readlines() # aqui será criado uma lista onde cada linha do código será armazenado em uma posição na lista.

print('conteúdo da lista criado apartir do arquivo .txt: ', listadelinhas, '\n')

for i in listadelinhas:
  print('lista separada em linhas: ', i)




# Exercicício:

'''
Faça um programa que receba o peso de 7 pessoas. Calcule e mostre:
    * a quantidade de pessoas acima de 90kg
    * a média dos pesos das pessoas
'''

def AcimaDoPesoEmedias():
  mensagens = [
        "Digite o 1º valor: ",
        "Digite o 2º valor: ",
        "Digite o 3º valor: ",
        "Digite o 4º valor: ",
        "Digite o 5º valor: ",
        "Digite o 6º valor: ",
        "Digite o 7º valor: "
    ]
  Maior90 = 0
  cont = 0
  MediaPesos = []
  for cont in range(7):
        valor = float(input(mensagens[cont]))
        MediaPesos.append(valor)
        if valor > 90:
          Maior90 += 1
  print('\n')
  MediaPesos = (sum(MediaPesos)/len(MediaPesos))
  return print(f'Quantidade de pessoas acima do peso: {Maior90} \n\nMédia dos pesos é: {round(MediaPesos, 2)} ')

AcimaDoPesoEmedias()



#Exercício:

'''
Faça um programa que mostre o resultado do fatorial de n (n!), que o usuário
digitar.
ex: 5! = 5*4*3*2*1
'''
def ListaFatorial (n = int(input('digite o valor do fatórial a ser calculado: '))):
  fator = []
  for cont in range(n):
    fator.append(n-cont)
  for i in range(len(fator)):
    fator[i] *= fator[i-1]
  print('resultado do fatorial: ', max(fator), '\n')

ListaFatorial()

#forma mais limpa de resolver:

x = int(input('digite fatorial: '))
fatorial = 1
for i in range(x, 0 , -1):
  fatorial *= i
print(f'resultado do fatorial: {fatorial}\n')




'''
Para representar-mos o tipo literal, Hexadecimal e Octal, utilizamos respectiva
mente: 0x e 0o (zero e x e zero o), seguida de uma sequecia numerica.
Para notação cientifica utiliza-se o E depois do numero a ser potencializado e o
valor da potência: Ex: 4E5 (4 vezes 10 elevado a 5 ou 4x10⁵ ou 400000)
O mesmo vale para numeros muito pequenos que nesse caso depois do E deve-se colocar
o sinal negativo. Ex: 3E-6 (3 vezes 10 elevado a menos 6 ou 3x10⁻⁶ ou 0.000006)
'''

print(f'Representação do valor 123 em Hexadecimal: {0x123}' )
print(f'Representação do valor 123 em Octal: {0o123}')
print(f'3 elevado a 8: {3E8}')
print(f'3 elevado a -8: {0.00000003}')






'''
operadores matemáticos e booleano

+ -> utilizado para soma e concatenação
- -> utilizado para subtração
* -> utilizado para multiplicação
/ -> utilizado para divisão
// -> barras duplas é utilizado para divisão onde o resultado será a parte interia do numero. Ex: 9//4 = 2 e não  = 2.25
% -> utilizado para o resto de uma divisão. Ex: 11%5 = 1 (resto 1)
** -> asteristico duplo utilizado para potenciação. EX: 3**5(3 elevado a 5).
operadores booleanos são representados pelas palavras reservadas: True e False

'''

print(f'somando dois numeros: 10+3= {10+3}')
print('concatenando duas string: ', 'string1-' + 'string2')
print(f'subtraindo dois numeros: 7-5= {7-5}')
print(f'multiplique dois numeros: 3*9= {3*9}')
print(f'divida dois numeros: 20/4= {20/4}')
print(f'divida dois numeros com casa decimal: 20./4= {20/4}') # só acrecentando um ponto em algum dois numeros isso já indicara que se trata de um float.
print(f'imprima o resto da divisão: 13/5= {13%5}')
print(f'resultado da potência: 3³ = {3**3}')
print(f'verdadeiro ou falso: 50>25? {50>25}')
print(f'verdadeiro ou falso: True>False? {True>False}') #Lembrando que True tem valor 1 e False tem valor 0. por isso que True>False é True pois 1>0
print(f'a seguinte afirmação é verdadeira ou falsa: {5+(5*(10/2)) > 4*(15//5)}')

'''
Hierarquia dos operadores em Python

prioridade     operador
1               +, -              unário Ex: +2 ou -2
2               **
3               *, /, //, %
4               +, -              binário Ex: 2+2 ou 2-2

Caso tenha operadores de mesma prioridade resolve-se da esquerda para a direita. Ex: 2*3%5 = 6%5 = 1
para o caso de potencia resolve-se da direita para a esquerda. Ex: 2**2**3 = 2**8 = 256
Caso queira arbitrar a ordem de prioridades utiliza-se os parenteses ().
'''




