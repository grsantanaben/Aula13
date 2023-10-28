# Aula 13
# **VERIFICAÇÃO DE STRINGS COM PYTHON**

# texto = 'Python é uma linguagem de programação. Python é Simples.Python é organizado. Python é uma excelente linguagem'

print (texto.count('é'))
print (texto.find('Python', 25,50))
print (texto.rfind('lingua'))
print (texto.index('é'))
print (texto.rindex('é'))

#Use os métodos .startswith() e .endswith() para verificar se uma string começa ou termina com uma determinada substring.

texto = "Isso é uma string de exemplo"
if texto.startswith("Isso"):
    print("A string começa com 'Isso'.")

if texto.endswith("exemplo"):
    print("A string termina com 'exemplo'.")


texto = 'Olá Mundo!'
texto_centro = texto.center(150)
texto_centro_2 = texto.center(20,'*')
texto_esquerda = texto.ljust(10)
texto_direita = texto.rjust(120)
print(texto_direita)
print(f'**{texto_esquerda}*{texto_direita}**')

nomes = 'João Paulo/Maria Pauloa'
print (nomes.split('/'))

#Exercicios

#Exercício 1: Escreva um programa que verifique se a palavra "python" está presente na string "Estou aprendendo Python".
texto = 'Estou aprendendo Python'
if "Python" in texto:
 print('Existe a palavra Python no texto')
else:
  print('Não existe')

#exercício 2: Escreva um programa que peça ao usuário para digitar seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula).
nome = input('Digite seu nome: ')
if nome.startswith('A'):
  print('Seu nome é', nome)
else:
  print('Nome não começa com a letra A')
  
#Exercício 3: Escreva um programa que peça ao usuário para digitar uma senha e verifique se a senha contém pelo menos 8 caracteres.

senha = input('Digite uma senha: ')
tamanho = len(senha)
if tamanho >= 8:
  print('Senha OK.')
else:
  print('Senha com menos de 8 caracteres')

# Exercício 4: Escreva um programa que peça ao usuário para digitar um número e verifique se o número é uma representação numérica (não contém letras ou símbolos).
numero = input('Digite um número: ')
if numero.isnumeric():
  print ('Apenas numeros ')
else:
  print('Atenção - Digite apenas numeros')
  
#Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vezes a letra "a" (maiúscula ou minúscula) aparece na frase.

frase = input('Escreva uma frase:')
contador = frase.count('a')
print  ('Nesta frase contém', contador, 'Letras')