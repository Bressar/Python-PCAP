#!/usr/bin/env python3 

""" module1.py - Exemplo de  Python module """ 

""" A linha começando com #! tem muitos nomes - pode ser chamada de shabang, shebang, hashbang, poundbang ou até mesmo hashpling. O nome em si não significa nada aqui - seu papel é mais importante. Do ponto de vista do Python, é apenas um comentário, pois começa com #. Para sistemas operacionais Unix e Unix-like (incluindo MacOS), essa linha instrui o sistema operacional sobre como executar o conteúdo do arquivo (em outras palavras, qual programa precisa ser lançado para interpretar o texto). Em alguns ambientes (especialmente aqueles conectados a servidores web), a ausência dessa linha causará problemas;
Uma string (talvez multilinha) colocada antes de qualquer instrução do módulo (incluindo importações) é chamada de doc-string e deve explicar brevemente o propósito e o conteúdo do módulo;
As funções definidas dentro do módulo (suml() e prodl()) estão disponíveis para importação;
Usamos a variável __name__ para detectar quando o arquivo é executado de forma autônoma e aproveitamos essa oportunidade para realizar alguns testes simples. """

# já com a privacidade configurada: usando  __

__counter = 0


def sumlist(the_list): # o contador recebe a soma de todos os números da lista
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum


def prodlist(the_list): # o contador recebe o produto de todos os números da lista
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod


if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)] # cria a lista [1,2,3,4,5] -> a soma dará 15 e a multiplicação 120
  print(sumlist(my_list) == 15)
  print(prodlist(my_list) == 120)
  
