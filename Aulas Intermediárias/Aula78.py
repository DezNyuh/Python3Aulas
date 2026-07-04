s1 = set() #vazio
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s2 = {1, 2, 3, 3, 3, 3, 3, 1} # com dados
s2 = set(l1)
l2 = list(s2)
print(l2)
s1 = {1, 2, 3}
print(3 not in s1)

for numero in s1:
    print(numero)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
#s1.clear() # descarta todas 
s1.discard('Olá mundo') # descarta um especifico
s1.discard('Luiz')
print(s1)


#operadores úteis:
# união '|' unon - une
# interseccção '&'- itens presente em ambos
# diferença '-' itens presentes apenas no set da esquerda
# diferença simétrica '^' itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s2 ^ s1
print(s3)