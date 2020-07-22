# comando de entrada de dados
ano = int(input("Digite um ano para checar se é bissexto \n"))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            # comando de saída de dados
            print ("{0} é ano bissexto".format(ano))
        else:
            # comando de saída de dados
            print("{0} não é ano bissexto".format(ano))
    else:
        # comando de saída de dados
        print("{0} é ano bissexto".format(ano))
else:
    # comando de saída de dados
    print("{0} não é ano bissexto".format(ano))

