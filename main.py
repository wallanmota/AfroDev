from data import *
from functions import *
import matplotlib.pyplot as plt


clear()
valormenu = menu()

invalid_value = 'Valor informado inválido!'
enter_number = 'Por favor digite um número!'
option = 'Digite a opção desejada: '

# Sub Menu 1
if valormenu == 1:
    print('\nSub Menu Atletas:')
    print('1 - Total de atletas participantes\n2 - Total de participantes homens\n'
          '3 - Total de participantes mulheres\n4 - Total de participantes por esporte\n'
          '5 - Pesquisar atletas por nome')
    sub1 = entrada()
    sub1 = submenu(sub1)
    if sub1 == 1:
        clear()
        print(f'\nO total de atletas participantes é: {total_atletas}\n')
        voltar()
    elif sub1 == 2:
        clear()
        print(f'\nO total de participantes homens é: {male}\n')
        voltar()
    elif sub1 == 3:
        clear()
        print(f'\nO total de participantes mulheres é: {female}\n')
        voltar()
    elif sub1 == 4:
        clear()
        print(f'Total de participantes por esporte:\n{total_discipline}')
        voltar()
    elif sub1 == 5:
        atleta()
        voltar()
    else:
        print(invalid_value)
        voltar()

# Sub Menu 2
elif valormenu == 2:
    print('Sub Menu Medalhas:')
    print('1 - Total de medalhas por país\n2 - Ranking por medalhas totais\n'
          '3 - Mais medalhas\n4 - Menos medalhas')
    sub2 = entrada()
    sub2 = submenu(sub2)
    if sub2 == 1:
        clear()
        print(f'\nTotal de medalhas por país:\n {total_medals.to_string(index=False)}\n')
        voltar()
    elif sub2 == 2:
        clear()
        print(f'\nRanking por medalhas totais:\n {ranking_top10.to_string(index=False)}\n')
        grafico = grafico()
        if grafico == '1':
            ranking_top10.groupby("Team/NOC")["Total"].sum().sort_values(ascending=True).plot.barh(
                title="Mais medalhas")
            plt.show()
        voltar()
    elif sub2 == 3:
        clear()
        print('Sub Menu Medalhas/Mais medalhas:')
        print('1 - País com mais medalhas de Ouro\n2 - País com mais medalhas de Prata\n'
              '3 - País com mais medalhas de Bronze')
        while True:
            sub2_mais = input(option)
            try:
                sub2_mais = int(sub2_mais)
                clear()
                break
            except Exception:
                if sub2_mais != sub2_mais.isnumeric():
                    print(enter_number)
                else:
                    break
        if sub2_mais == 1:
            clear()
            print(f'\nPaís com mais medalhas de Ouro:\n {gold_more}\n')
            voltar()
        elif sub2_mais == 2:
            clear()
            print(f'\nPaís com mais medalhas de Prata:\n {silver_more}\n')
            voltar()
        elif sub2_mais == 3:
            clear()
            print(f'\nPaís com mais medalhas de Bronze:\n {bronze_more}\n')
            voltar()
        else:
            print(invalid_value)
            voltar()
    elif sub2 == 4:
        clear()
        print('Sub Menu Medalhas/Menos medalhas:')
        print('1 - País com menos medalhas de Ouro\n2 - País com menos medalhas de Prata\n'
              '3 - País com menos medalhas de Bronze')
        while True:
            sub2_menos = input(option)
            try:
                sub2_menos = int(sub2_menos)
                clear()
                break
            except Exception:
                if sub2_menos != sub2_menos.isnumeric():
                    print(enter_number)
                else:
                    break
        if sub2_menos == 1:
            clear()
            print(f'\nPaís com menos medalhas de Ouro:\n {gold_less}\n')
            voltar()
        elif sub2_menos == 2:
            clear()
            print(f'\nPaís com menos medalhas de Prata:\n {silver_less}\n')
            voltar()
        elif sub2_menos == 3:
            clear()
            print(f'\nPaís com menos medalhas de Bronze:\n {bronze_less}\n')
            voltar()
        else:
            print(invalid_value)
            voltar()
    else:
        print(invalid_value)
        voltar()

# Sub Menu 3
elif valormenu == 3:
    print('Sub Menu Esportes: ')
    print('1 - Lista com esportes participantes\n2 - Lista de esportes com mais homens que mulheres\n'
          '3 - Lista de esportes com mais mulheres que homens\n'
          '4 - Lista de espostes com a mesma quantidade de Homens e Mulheres\n'
          '5 - Quantos times por esporte cada país tem')
    sub3 = entrada()
    sub3 = submenu(sub3)
    if sub3 == 1:
        clear()
        print(f'\nLista com esportes participantes:\nNo total temos {qtd_disciplines} esportes.'
              f'\n\n{disciplines}\n')
        voltar()
    elif sub3 == 2:
        clear()
        print(f'\nLista de esportes com mais homens que mulheres:\n{disciplines_more_men.to_string(index=False)}\n')
        grafico = grafico()
        if grafico == '1':
            disciplines_more_men.groupby("Discipline")["Male"].sum().sort_values(ascending=True).plot.barh(
                title="Mais Homens")
            plt.show()
        voltar()
    elif sub3 == 3:
        clear()
        print(f'\nLista de esportes com mais mulheres que homens:\n{disciplines_more_women.to_string(index=False)}\n')
        grafico = grafico()
        if grafico == '1':
            disciplines_more_women.groupby("Discipline")["Female"].sum().sort_values(ascending=True).plot.pie(
                title="Mais Mulheres", autopct="%1.2f%%")
            plt.show()
        voltar()
    elif sub3 == 4:
        clear()
        print(f'\nLista de espostes com a mesma quantidade de Homens e Mulheres:\n{disciplines_same_amount}\n')
        voltar()
    elif sub3 == 5:
        clear()
        print(f'\nQuantos times por esporte cada país tem:')
        print(teams_list)

        while True:
            modal = input('\nDigite o esporte desesejado da lista acima para ver a '
                          'quatidade de equipes de cada país: ').strip().title()
            try:
                teams.loc[modal]
            except KeyError:
                print('\n*** Esporte informado não foi encontrado. Tente novamente! ***')
            else:
                clear()
                print(f'\n{modal}\n{teams.loc[modal]}\n')
                break
        voltar()
    else:
        print(invalid_value)
        voltar()

# Sub Menu 4
elif valormenu == 4:
    print('Sub Menu Treinadores: ')
    print('1 - Quantidade de treinadores por país\n2 - País com a maior quantidade de treinadores\n'
          '3 - Quantidade de treinadores por esporte')
    sub4 = entrada()
    sub4 = submenu(sub4)
    if sub4 == 1:
        clear()
        print(f'\nQuantidade de treinadores por país:\n{coaches_country}\n')
        voltar()
    elif sub4 == 2:
        clear()
        print(f'\nPaís com a maior quantidade de treinadores:\nPais: {more_coaches[0]}\n'
              f'Quantidade de treinadores: {more_coaches[1]}\n')
        voltar()
    elif sub4 == 3:
        clear()
        print(f'\nQuantidade de treinadores por esporte:\n{coaches_discipline}\n')
        voltar()
    else:
        print(invalid_value)
        voltar()

else:
    print(invalid_value)
    voltar()
