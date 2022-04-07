#Livro Introdução à programação com python: algoritmos e lógica de programação para iniciantes.
#Exercício 03-12

#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para viagem.

distancia= float(input("Digite a distância em km:"))
velocidade_media= float (input("Digite a velocidade média em km/h:"))
tempo= distancia/velocidade_media
print("O tempo estimado é de %5.2f horas" % tempo)

# Opcional exibir o tempo em horas, minutos e segundos.

tempo_s= int(tempo* 3600) #Convertido de horas para minutos
horas= int(tempo_s/3600) #Parte inteira
tempo_s= int(tempo_s % 3600)
minutos= int(tempo_s / 60)
segundos= int(tempo_s % 60)
print("%05d:%02d:%02d" % (horas, minutos, segundos))