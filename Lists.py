#lista = [10, 20, 30, 40]
#lista[2] = 700
#del lista[2]
#print(lista[2])
#lista.append(50)
#lista.pop()
#lista.append(60)
#lista.append(70)
#del lista[-1]
#lista.insert(100, 4)
#print(lista[4])


# ------------------------

#lista_a = [1, 2, 3]
#lista_b = [4, 5, 6]
#lista_c = lista_a + lista_b
#lista_d = lista_a.extend(lista_b)
#print(lista_c)


# -----------------

lista_a = ['Luiz', 'Maria', 1, True, 1.5]
lista_b = lista_a

lista_a[0] = 'something'
print(lista_a)
print(lista_b)