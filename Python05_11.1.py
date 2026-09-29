SetA = set(('3', '14', '15', '9', '26', '5', '35', '9'))
SetB = set(('60', '22', '14', '0', '9'))
print(f'Esse é o set A: {SetA}\n e esse é o set b: {SetB}')
print(f'Essa é a intersecção: {SetA & SetB}\nEssa é a diferença de A para B: {SetA - SetB}\nEssa é a diferença de B para A: {SetB - SetA}\nEssa é a união de ambos: {SetA|SetB}\nEssa é a diferença simétrica entre deles: {SetA^SetB}')

