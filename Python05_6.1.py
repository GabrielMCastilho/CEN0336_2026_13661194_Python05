coisas_favoritas = {'Livro':'RedRising: Golden Son','Tipo musical':'Rock','arvore':'Ipê'}
print(coisas_favoritas)


# Parte 5 do script: adicionar uma nova chave e valor e printar ele

coisas_favoritas['organismo'] = 'Trichoderma'
fav_thing = 'organismo'
print(coisas_favoritas[fav_thing])

# Parte 6 do script: Deixar o usuário escolher a chave
chaves = coisas_favoritas.keys()
print('Escolha uma das chaves abaixo para saber qual é o favorito:')
for chave in chaves:
    print('-', chave)
fav_thing = input()
print(coisas_favoritas[fav_thing])
