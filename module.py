
print("Eu gosto de ser um módulo.")
print(__name__)

counter = 0 # usando um contador

if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")

""" 
quando você executa um arquivo diretamente, sua variável __name__ é definida como __main__;
quando um arquivo é importado como um módulo, sua variável __name__ é definida como o nome do arquivo (excluindo .py) """

# No caso aqui: __main__
# "I prefer to be a module."