# idade, nasc, ano, niver_mes, mes, niver_dia, dia,
# i, j, dias, d, idade_dias, resto_ano, meses, days
# bis: logico

print("Idade, COMPLETO")

# só em anos
idade = int(input("Informe a idade do indivíduo: "))
# verificação
nasc = int(input("Informe o ano de nascimento: "))
atual = int(input("Informe o ano atual: "))
niver_mes = int(input("Informe o mês de aniversário: "))
mes = int(input("Informe o mês atual: "))
niver_dia = int(input("Informe o dia de aniversário: "))
dia = int(input("Informe o dia atual: "))

bis = bool(input("Informe se é ano bissexto: "))

# idade a cada 4 anos idade_dias < - + 1 dia(anos bissextos)

# o indivíduo nasceu
if ano < nasc:
    nasc = int(input("Informe novamente o ano de nascimento: "))
    atual = int(input("Informe novamente o ano atual: "))

# validade do mês
if niver_mes < 1 or niver_mes > 12:
    niver_mes = int(input("Informe novamente o mês de aniversário: "))
if mes < 1 or mes > 12:
    mes = int(input("Informe novamente o mês atual: "))

# Início do bloco para o mês de aniversário
i = niver_mes

print("Mes de aniversário: ")
# fevereiro
if i == 2:
    print ("Fevereiro")
    if bis == False:
        print("Ano não bissexto")
        dias = 28
    else: # True
        print("Ano bissexto")
        dias = 29

# abril, junho, setembro, novembro
if i == 4 or i == 6 or i == 9 or i == 11:
    dias = 30
else: # janeiro, março, maio, julho, outubro, dezembro
    dias = 31

# meses impressos exceto fevereiro
if i == 1:
    print("Janeiro")
if i == 3:
    print("Março")
if i == 4:
    print("Abril")
if i == 5:
    print("Maio")
if i == 6:
    print("Junho")
if i == 7:
    print("Julho")
if i == 8:
    print("Agosto")
if i == 9:
    print("Setembro")
if i == 10:
    print("Outubro")
if i == 11:
    print("Novembro")
if i == 12:
    print("Dezembro")

# Fim do bloco para o mês de aniversário

# Início do bloco para o mês atual
j = mes

print("Mes atual: ")
# fevereiro
if j == 2:
    print ("Fevereiro")
    if bis == False:
        print("Ano não bissexto")
        d = 28
    else: # True
        print("Ano bissexto")
        d = 29

# abril, junho, setembro, novembro
if j == 4 or j == 6 or j == 9 or j == 11:
    d = 30
else: # janeiro, março, maio, julho, outubro, dezembro
    d = 31

# meses impressos exceto fevereiro
if j == 1:
    print("Janeiro")
if j == 3:
    print("Março")
if j == 4:
    print("Abril")
if j == 5:
    print("Maio")
if j == 6:
    print("Junho")
if j == 7:
    print("Julho")
if j == 8:
    print("Agosto")
if j == 9:
    print("Setembro")
if j == 10:
    print("Outubro")
if j == 11:
    print("Novembro")
if j == 12:
    print("Dezembro")

# Fim do bloco para o mês atual

# Validade de dias mês aniversário
if niver_mes == i or mes == j:
   if niver_dia < 1 or niver_dia > dias:
       niver_dia = int(input("Informe novamente o dia de aniversário: "))
   if dia < 1 or dia > d:
       dia = int(input("Informe novamente o dia atual: "))

# idade a cada 4 anos idade_dias < - + 1 dia(anos bissextos)

if niver_mes == mes:
    if niver_dia == dia:
        idade_dias < - idade * 365 + int(idade / 4)
        print(idade_dias, " idade em dia(s).")
    elif niver_dia < dia:
        idade_dias < - idade * 365 + int(idade / 4) + (dia - niver_dia)
        print(idade_dias, " idade em dia(s).")
    else: # niver_dia > dia:
        idade_dias < - idade * 365 + int(idade / 4) + (12 - 1) * 30 + (d - (niver_dia - dia))
        print(idade_dias, " idade em dia(s).")
elif niver_mes < mes:
    if niver_dia == dia:
        idade_dias < - idade * 365 + int(idade / 4) + (mes - niver_mes) * 30
        print(idade_dias, " idade em dia(s).")
    elif niver_dia < dia:
        idade_dias < - idade * 365 + int(idade / 4) + (mes - niver_mes) * 30 + (dia - niver_dia)
        print(idade_dias, " idade em dia(s).")
    else: # niver_dia > dia:
        idade_dias < - idade * 365 + int(idade / 4) + (mes - niver_mes - 1) * 30 + (dias - (niver_dia - dia))
        print(idade_dias, " idade em dia(s).")
else: # niver_mes > mes:
    if niver_dia == dia:
        idade_dias < - idade * 365 + int(idade / 4) + 12 - (niver_mes - mes) * 30
        print(idade_dias, " idade em dia(s).")
    elif niver_dia < dia:
        idade_dias < - idade * 365 + int(idade / 4) + 12 - (niver_mes - mes) * 30 + (dia - niver_dia)
        print(idade_dias, " idade em dia(s).")
    else: # niver_dia > dia:
        idade_dias < - idade * 365 + int(idade / 4) + 12 - (niver_mes - mes - 1) * 30 + (d - (niver_dia - dia))
        print(idade_dias, " idade em dia(s).")

ano = int(idade_dias / 365)
print('anos = ', ano)
resto_ano = idade_dias % 365
print('o que restou em dias = ', resto_ano)
meses = int(resto_ano / 30)
print('meses = ', meses)
days = resto_ano % 30
print('dias = ', days)
print(ano, " ano(s), ", meses, " mes(es) e ", days, " dia(s)")
