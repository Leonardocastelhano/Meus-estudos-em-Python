nome= input('Qual é o seu nome?')
print('Prazer em te conhecer{}!'.format(nome))
print('Prazer em te conhecer{:20}!'.format(nome))
print('Prazer em te conhecer{:>20}!'.format(nome))
print('Prazer em te conhecer{:<20}!'.format(nome))
print('Prazer em te conhecer{:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di =n1//n2
e = n1**n2
print('A soma é {}, o produto é {}, a divisão é {}'.format(s,m,d))
print('Divisão inteira {} e potência {}'.format(di,e))
print('A soma é {}, o produto é {}, a divisão é {:.3f}'.format(s,m,d))
print('A soma é {}, o produto é {}, a divisão é {:.3f}'.format(s,m,d), end=" ")
print('A soma é {},\n o produto é {},\n a divisão é {:.3f}'.format(s,m,d), end=" ")











