#import module
#print(module.counter) # imprimindo a variável contador do módulo


from module1 import sumlist, prodlist
# print(module1.__counter) # imprimindo a variável contador do módulo

zeroes = [0 for i in range(5)]# [0,0,0,0,0]
ones = [1 for i in range(5)]# [1,1,1,1,1]
print(sumlist(zeroes))
print(prodlist(ones))



""" 
Ao importar o modulo uma pasta é criada: __pycache__
Há um arquivo chamado (mais ou menos) module.cpython-xy.pyc, 
onde x e y são dígitos derivados da sua versão do Python 
(por exemplo, serão 3 e 12 se você estiver usando o Python 3.12).

O nome do arquivo é o mesmo que o nome do seu módulo (neste caso, module). 
A parte após o primeiro ponto indica qual implementação do Python criou o arquivo (CPython aqui)
e seu número de versão. A última parte (pyc) vem das palavras Python e compilado.

Quando o Python importa um módulo pela primeira vez, ele traduz seu conteúdo para uma forma meio compilada.

O arquivo não contém código de máquina – é um código semi-compilado interno do Python, pronto para ser executado pelo interpretador do Python. Como tal, o arquivo não requer muitas das verificações necessárias para um arquivo de código-fonte puro, a execução começa mais rápido e também roda mais rápido.

Graças a isso, cada importação subsequente será mais rápida do que interpretar o texto-fonte do zero.

O Python é capaz de verificar se o arquivo-fonte do módulo foi modificado (neste caso, o arquivo pyc será reconstruído) ou não (caso em que o arquivo pyc pode ser executado de imediato). Como esse processo é totalmente automático e transparente, você não precisa se preocupar com isso.

Nota: a inicialização ocorre apenas uma vez, quando o primeiro import é realizado, então as atribuições feitas pelo módulo não são repetidas desnecessariamente."""


# quando você executa um arquivo diretamente, sua variável __name__ é definida como __main__;
# quando um arquivo é importado como um módulo, sua variável __name__ é definida como o nome do arquivo (excluindo .py) 

# No caso aqui: module
# "I like to be a module."

