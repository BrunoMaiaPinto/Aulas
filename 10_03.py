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

# numLista = [1,2,3,4,5,6,7,8,9,10]
# listaPares = list(filter(lambda x: x % 2 == 0, numLista))
# listaPares = list(filter(lambda x: not x % 2 , numLista))
# print(listaPares)

# from functools import reduce

# produto = reduce(lambda x,y: x * y, numLista)
# print(produto)

# listaPalavras = ['Feijão', 'Tomate', 'Arroz', 'Pão']
# lenPalavras = list(sorted(listaPalavras, key=len))
# print(lenPalavras)

# print('Todos são pares' if all(map(lambda x: x > 0, numLista)) else 'Pelo menos um é negativo')

# print(any(map(lambda x: x % 2 == 0, numLista)))

# combinado = list(zip(numLista, listaPalavras))
# print(combinado)

# lista = [2,22,14,89,65,21,3,4,5]
# quadrados = list(map(lambda x: x**2, lista))
# print(quadrados)

# listaPalavras = ['Banana', 'Maça', 'Laranja', 'Ananas', 'Uva']
# palavras5 = list(filter(lambda x : len(x) > 5, listaPalavras))
# print(palavras5)

# quadradosPares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, lista)))

# print(quadradosPares)

# dicionario = [{'cão': 'dog'}, {'gato': 'cat'}, {'peixe': 'fish'}]
# diciOrdenado = sorted(list(map(lambda x: x.keys(), dicionario)))
# print(diciOrdenado)

# alunos=[
#   {'nome':'Bruno', 'nota': 15},
#   {'nome':'João', 'nota': 1},
#   {'nome':'Nuno', 'nota': 20}
#   ]

# alunos_ordenado = sorted(alunos, key=lambda aluno: aluno['nota'], reverse=True)

# for aluno in alunos_ordenado:
#   print(f'{aluno['nome']}: {aluno['nota']}')

# class Rectangulo:
#   def __init__(self, largura, altura):
#     self.largura = largura
#     self.altura = altura

#   def calcArea(self):
#     return self.largura * self.altura
  
#   def calcPermitro(self):
#     return 2 * (self.largura + self.altura)
  

# rect = Rectangulo(5,12)

# print(f'Área: {rect.calcArea()}')
# print(f'Perímetro: {rect.calcPermitro()}')

# class ContaBancaria:
#   def __init__(self, saldo):
#     self.saldo = saldo

#   def deposito(self, deposito):
#     self.saldo += deposito

#   def levantamento(self, levantamento):
#     self.saldo -= levantamento
  
#   def consultarSaldo(self):
#     return self.saldo

# conta = ContaBancaria(0)

# conta.deposito(100)
# conta.levantamento(60)

# print(conta.consultarSaldo())

# from functools import reduce

# class Aluno:
#   def __init__(self, nome, numero, notas):
#     self.nome = nome
#     self.numero = numero
#     self.notas = notas
  
#   def calcMedia(self):
#     return reduce(lambda x, y: x + y, self.notas) / len(self.notas)
#     # return sum(self.notas) / len(self.notas)
  
#   def aprovado(self):
#     return f'{self.calcMedia():.1f} Aprovado' if self.calcMedia() >= 10 else f'{self.calcMedia():.1f} Reprovado'

# aluno = Aluno('Bruno', 89, [10, 11, 12, 13, 9, 8])
# aluno2 = Aluno('Aline', 35, [0, 1, 2, 3, 9, 8])

# print(aluno.aprovado())
# print(aluno2.aprovado())