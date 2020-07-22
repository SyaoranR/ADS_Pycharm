# comando de sa�da de dados
print("Média ponderada de 5 notas")
n = 0 # numerador
d = 0 # denominador
mp = 0 # média ponderada

# laço de repetição for i no limite (início, fim, passo)
# python permite que 'vetores' sejam dinâmicos (tamanho variável)
for i in range (1, 6, 1):
    # comando de entrada de dados
    x = int(input('Informe a nota '))
    print('Nota ', i, ': ', x)
    n = n + (x * i)
    print("n = ", n)
    d = d + i
    print("d = ", d)
mp = n / d
# %4.2f = formatação para floats duas casas decimais, 4 = ?
print('Média ponderada das 5 notas : %4.2f' % mp)

