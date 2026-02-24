import os

print('Selecione uma opção')
lista = [] 

opc = input('[i]nsira, [d]elete, [l]istar: ')
while True:
    if opc == 'i':
        os.system('clear')
        item = input('Adicione algo a lista: ')
        lista.append(item)
        print(lista)
        item = input('Adicionar outra coisa?')
        if item == 'sim':
            item = input('Adicone algo a lista: ')
            lista.append(item)
            pass
        if item == 'nao':
            pass

    elif opc == 'd':
        print(lista)
        item = input('Digite algo para remover: ')
        if item in lista:
            lista.remove(item)

    elif opc == 'l':
        os.system('clear')
        print(lista) 

    else:
        print('Por Favor escolha, i, d ou l') 