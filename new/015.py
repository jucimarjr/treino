print('='*15)
d = float(input('Por quantos dias você alugou o carro?: '))
km = float(input('Quantos KM você rodou com o carro?: '))
print('O valor cobrado será de R${:.2f}'.format((d*60)+(km*0.15)))
print('='*15)
