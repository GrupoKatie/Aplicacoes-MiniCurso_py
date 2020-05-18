def funcVelo(velocidade, tempo, espaco):
  velocidadeMedia = espaco / tempo
  aceleracao = velocidadeMedia / tempo
  print(velocidadeMedia)
  print(aceleracao)
  
  
espaco = float(input())
tempo = float(input())
velocidade = float(input())

funcVelo(velocidade, tempo, espaco)
