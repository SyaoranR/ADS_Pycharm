# comando de sa�da de dados
print("S�rie Fibonacci")
# primeiros dois valores da s�rie
a = 1
b = 1
# comando de entrada de dados
n = int(input('Informe quantos n�meros ter� a s�rie: '))
# la�o de repeti��o for i no limite (in�cio, fim, passo)
# python permite que 'vetores' sejam din�micos (tamanho vari�vel)
for i in range (1, n, 1):
    c = a + b
    print("c = ", c)
    a = b
    b = c
print("resultado = ", c)

