# lista de exerc�cios 0
print("1 Fatorial")
def fatorial(n):
    if (n > 1):
        fat = n * fatorial(n-1)
    else:
        fat = 1
    return fat

n = int(input("Entre com o valor de n: "))
y = n

for i in range (n, 1, -1):
    print("{} * {} = {}".format
              (y, i-1, y * (i-1)))
    y = y * (i - 1)

print("Valor do fatorial = ", fatorial(n))

print("")
print("2 S�rie Fibonacci")
print("")

def fibonacci(m):
    a = 1
    b = 1
    vet = []
    # como pode ser visto abaixo, em python o preenchimento do
    # 'vetor' n�o ocorre da forma abaixo, fora que o termo
    # 'vetor' n�o existe em python, mas sim listas
    # vet[0] = a
    # vet[1] = b
    # observe como se preenche o vetor
    vet.append(a)
    vet.append(b)

    # 2 porque o as duas primeiras posi��es j� s�o ocupadas
    # pelos n�meros 1 na s�rie fibonacci
    for i in range(2, m, 1):
        print("a = ", a, " b = ", b)
        c = a + b
        vet.append(c)
        # "{} * {} = {}".format(num, c, num * c)
        print("{} + {} = {}" .format(a, b, a + b))
        a = b
        b = c
    # return c
    # como pode ser visto abaixo, em python nem a impress�o
    # do 'vetor' � feito da forma convencional "vetor[indice]"
    # return vet[i]
    # mas simplesmente a vari�vel "vet", mais uma vez afirmando
    # que se trata de uma lista de dados, n�o de um vetor
    return vet

m = int(input("Entre com o valor de m: "))
print("S�rie de fibonacci = ", fibonacci(m))

print("")
print("3 N�mero Primo")
print("")

x = int(input('Informe um n�mero inteiro: '))
cont = 0
# deve incluir o zero (x, zero, passo -1)
for m in range(x, 0, -1):
    if x % m == 0:
        cont = cont + 1
if cont == 2:
   print('quantos n�meros dividem ', x,' = ', cont)
   print('O n�mero ', x, ' � primo')
else:
   print('quantos n�meros dividem ', x,' = ', cont)
   print('O n�mero ', x, ' n�o � primo')
