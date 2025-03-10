# x = int(input('Insira um numero: '))

# funcao = lambda x: 10 <= x <= 20

# print(f'{x} está no intervalo' if funcao(x) else f'{x} não está no intervalo')

# def verOrdenar(a,b,c):
#   if a < b < c:
#     return 'Ordem Crescente'
#   else:
#     return 'Não estão em orderm'

# print(verOrdenar(3,2,1))
# print(verOrdenar(1,3,2))
# print(verOrdenar(1,2,3))

# lista = [0,2,3,0,4,5,'', []]

# def firstTrue(lista):
#   for el in lista:
#     if el:
#       return el
    
# print(firstTrue(lista))

# def countFalse(lista):
#   count = 0
#   for el in lista:
#     if not el:
#       count+=1
#   return count

# print(countFalse(lista))

# x = int(input('Insira um numero: '))

# print(f'{x} é par' if x % 2 == 0 else f'{x} é ímpar')

# def notas(nota):
#   return 'Aprovado' if nota >= 10 else 'Reprovado'

# print(notas(15))

# def palavraFrase(frase, palavra):
#   return f'{palavra} está na frase' if palavra.lower() in frase.lower() else f'{palavra} não está na frase'

# frase = 'Revelado pacto secreto entre Gyökeres e Sporting para a saída'
# palavra1 = 'Gyökeres'
# palavra2 = 'Porto'

# print(palavraFrase(frase, palavra1))
# print(palavraFrase(frase, palavra2))

# def vogalString(palavra):
#     for letra in palavra:
#       if letra.lower() in 'aeiou':
#         return 'Palavra com vogal'
#     return 'Palavra sem vogais'

# print(vogalString('cdAht'))
        
# quadrado = lambda x: x**2
# print(quadrado(5))

# celToFah = lambda tempCel: tempCel * (9/5) + 32

# print(celToFah(25))

# temperaturas = [15,25,30,12,5]

# temperaturasFah = list(map(celToFah, temperaturas))
# print(temperaturasFah)

numLista = [1,2,3,4,5,6,7,8,9,10]
listaPares = list(filter(lambda x: x % 2 == 0, numLista))
print(listaPares)

from functools import reduce

produto = reduce(lambda x,y: x * y, numLista)
print(produto)

listaPalavras = ['Feijão', 'Tomate', 'Arroz', 'Pão']
lenPalavras = list(sorted(listaPalavras, key=len))
print(lenPalavras)

print('Todos são pares' if all(map(lambda x: x > 0, numLista)) else 'Pelo menos um é negativo')

print(any(map(lambda x: x % 2 == 0, numLista)))

combinado = list(zip(numLista, listaPalavras))
print(combinado)