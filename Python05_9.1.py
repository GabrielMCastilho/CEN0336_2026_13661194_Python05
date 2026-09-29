coisas_favoritas = {'Livro':'RedRising: Golden Son','Tipo musical':'Rock','arvore':'Ipê'}
print(coisas_favoritas)


# Parte 5 do script: adicionar uma nova chave e valor

coisas_favoritas['organismo'] = 'Trichoderma'

# Parte 9 do script: loop que mostra chave e valor
for chave in chaves:
    print('Chave: ',chave,' Valor:', coisas_favoritas[chave])
