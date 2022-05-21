real = float(input('Quanto dinheiro você tem na carteira?R$'))
dolaramericano = real/4.88
dolarcanadense = real/3.80
euro= real/5.15
dolaraustraliano = real/3.44
euro = real/5.15
print('Com R${:.2f} você pode comprar EUA U${:.2f}'.format(real, dolaramericano))
print('Com R${:.2f} você pode comprar CAD U${:.2f}'.format(real, dolarcanadense))
print('Com R${:.2f} você pode compra AUD U${:.2f}.'.format(real, dolaraustraliano))
print('Com R${:.2f} você pode comprar Euro {:.2f}'.format(real, euro))



