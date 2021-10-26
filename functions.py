import os

enter_number = 'Por favor digite um número!'
option = 'Digite a opção desejada: '


# Funções de Menu
def entrada():
    entrance = input(option)
    return entrance


def menu():
    print('\n*** BEM VINDO AO SISTEMA DE ANÁLISE DE DADOS DAS OLIMPIADAS ***\n')
    print('1 - Atletas\n2 - Medalhas\n3 - Esportes\n4 - Treinadores')
    while True:
        menu_option = input(option)
        try:
            menu_option = int(menu_option)
            clear()
            return menu_option
        except Exception:
            if menu_option != menu_option.isnumeric():
                print(enter_number)
            else:
                break


def submenu(sub):
    while True:
        try:
            sub = int(sub)
            return sub
        except Exception:
            if sub != sub.isnumeric():
                print(enter_number)
                break
            else:
                break


# Grafico
def grafico():
    print('Digite qualquer tecla para sair!')
    grafic = input('1 - Para exibir grafico: ')
    return grafic


# Funçoes sistemicas
def voltar():
    print('Digite qualquer tecla para encerrar!')
    volta = input('0 - inicio: ')
    if volta == '0':
        clear()
        return os.system('python main.py')


def clear():
    os.system("clear")
    #os.system("cls") -> Usar assim caso for rodar no Windows
