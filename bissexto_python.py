# comando de entrada de dados
ano = int(input("Digite um ano para checar se � bissexto \n"))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            # comando de sa�da de dados
            print ("{0} � ano bissexto".format(ano))
        else:
            # comando de sa�da de dados
            print("{0} n�o � ano bissexto".format(ano))
    else:
        # comando de sa�da de dados
        print("{0} � ano bissexto".format(ano))
else:
    # comando de sa�da de dados
    print("{0} n�o � ano bissexto".format(ano))

