coisas_favoritas = {'Livro':'RedRising: Golden Son','Tipo musical':'Rock','arvore':'Ipê'}
print(coisas_favoritas)

#Parte 2 do script: printar o livro favorito

print(coisas_favoritas['Livro'])

# Parte 3 do script: printar o livro através de uma chave em uma variável pré-definida

livro_fav = 'Livro'
print(coisas_favoritas[livro_fav])

# Parte 4 do script: printar árvore favorita

print(coisas_favoritas['arvore'])

# Parte 5 do script: adicionar uma nova chave e valor e printar ele

coisas_favoritas['organismo'] = 'Trichoderma'
fav_thing = 'organismo'
print(coisas_favoritas[fav_thing])
