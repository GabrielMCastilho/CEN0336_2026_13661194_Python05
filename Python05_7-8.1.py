coisas_favoritas = {'Livro':'RedRising: Golden Son','Tipo musical':'Rock','arvore':'Ipê'}
print(coisas_favoritas)

# Parte 5 do script: adicionar uma nova chave e valor

coisas_favoritas['organismo'] = 'Trichoderma'

# Parte 7 e 8 
print('Qual é o seu organismo favorito?')
fav_thing = input()
coisas_favoritas['organismo'] = fav_thing
print('Essa é a lista resultante:', coisas_favoritas)
