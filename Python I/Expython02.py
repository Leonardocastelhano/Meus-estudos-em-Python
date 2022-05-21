a = int(input('Digite um número:'))
dobro=a*2
print('O dobro de', a , 'é', a*2)

a = int(input('Digite um número'))
dobro = a*2
print('O dobro de {} vale {}'.format(a, dobro))

a = int(input('Digite um número'))
dobro = a*2
triplo = a*3
raizquadrada = a**(1/2)
print('O dobro de {} vale {}'.format(a, dobro))
print('O triplo de {} vale {}'.format(a, triplo))
print('A raíz quadrada de {} vale {}'.format(a, raizquadrada))

print('O dobro de {} vale {}'.format(a, dobro))
print('O triplo de {} vale {}'.format(a, triplo))
print('A raíz quadrada de {} vale {:.2f}'.format(a, raizquadrada))

a= int(input('Digite um número'))
print('O dobro de {} vale {}'.format(a, (a*2)))
print('O triplo de {} vale {}'.format(a,(a*3)))
print('A raiz quadrada de {} vale {:.2f}'.format(a,(a**(1/2))))
print('Outro forma de calcular raiz quadrada é pow(n, (1/2)\n raiz quadrada de {} vale {:.2f}'.format(a, pow(a, (1/2))))
