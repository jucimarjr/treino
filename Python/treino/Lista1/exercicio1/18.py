print ("Exerc 18")

tamanho = float(input('Qual o tamanho do arquivo que você quer enviar: '))
velocidade = float(input('Qual a sua velocidade (em Mbps): '))

tamanhoBits = tamanho * 1024 * 1024 * 8
tempoSegundos = tamanhoBits / (velocidade * 1024 * 1024)
tempoMinutos = tempoSegundos / 60

print ('Tempo aproximado de download:', tempoMinutos, 'minutos')
