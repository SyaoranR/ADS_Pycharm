# lista de exercícios 2
print("7 Alf&Bet")
h1 = 1.5
h2 = 1.1
anos = 0

while h1 > h2:
    h1 = h1 + 0.02
    h2 = h2 + 0.03
    anos = anos + 1

if h2 > h1:
    h1 = h1 - 0.02
    h2 = h2 - 0.03
    anos = anos - 1

print('h1 = h2, altura 1 = %4.2f ' % h1, ' altura 2 = %4.2f' % h2)
print('anos = ', anos)

print("")
print("8 Ingressos")
print("")

i = 0
desp = 200
ingressos = 120
pr = 5.00

while pr >= 1.00:
    print("Lucro em ", i)
    lucro = pr * ingressos - desp
    print("Ingressos = " , ingressos)
    print("Preço = R$ %4.2f " % pr)
    print("Lucro = R$ %4.2f " % lucro)
    print('')
    ingressos = ingressos + 26
    pr = pr - 0.50
    i = i + 1

print("")
print("9 Idade em dias")
print("")

idade_dias = int(input("Informe a idade do indivíduo em dias: "))
# idade bruta e anos
ano = int(idade_dias / 365)
# resto_ano => dias a mais
resto_ano = idade_dias % 365
# mes(es), resto_ano >= 30
mes = int(resto_ano / 30)
# dias restantes, <30
dia = resto_ano % 30
print(ano, ' ano(s), ', mes, ' mes(es) e ', dia, ' dia(s).')
