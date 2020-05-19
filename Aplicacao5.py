def funcVelo(tempo, espaco):
  velocidadeMedia = espaco / tempo
  aceleracao = velocidadeMedia / tempo
  print(velocidadeMedia)
  print(aceleracao)
  
  
espaco = float(input())
tempo = float(input())

funcVelo(tempo, espaco)
