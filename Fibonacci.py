# comando de saída de dados
print("Série Fibonacci")
# primeiros dois valores da série
a = 1
b = 1
# comando de entrada de dados
n = int(input('Informe quantos números terá a série: '))
# laço de repetição for i no limite (início, fim, passo)
# python permite que 'vetores' sejam dinâmicos (tamanho variável)
for i in range (1, n, 1):
    c = a + b
    print("c = ", c)
    a = b
    b = c
print("resultado = ", c)

