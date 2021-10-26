import pandas as pd
import warnings
warnings.simplefilter("ignore")

df_athletes = pd.read_excel('db/Athletes.xlsx')
df_gender = pd.read_excel('db/EntriesGender.xlsx')
df_medals = pd.read_excel('db/Medals.xlsx')
df_coaches = pd.read_excel('db/Coaches.xlsx')
df_teams = pd.read_excel('db/Teams.xlsx')

# Total athletes
name = df_athletes['Name'].unique()
total_atletas = len(name)
# Total Men
male = df_gender['Male'].sum()
# Total Women
female = df_gender['Female'].sum()
# Total athletes by discipline
df_gender['Total'] = df_gender['Female'] + df_gender['Male']
total_discipline = (df_gender[['Discipline', 'Total']].to_string(index=False))


# Search Athletes by name
def atleta():
    while True:
        name_atl = input('\nDigite o nome do atleta: ').strip().upper()
        df_athletes2 = df_athletes.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
        df_athletes2['nome_atl'] = df_athletes2.Name.str.contains(name_atl)
        atl = df_athletes2.query("nome_atl == True")
        if df_athletes2.query("nome_atl == True").empty:
            print('\n*** Nome não encontrado! Tente novamente. ***')
        else:
            print(atl[['Name', 'NOC', 'Discipline']].to_string(index=False))
            break


# Total medals by country
df_medals['Total'] = df_medals['Gold'] + df_medals['Silver'] + df_medals['Bronze']
total_medals = df_medals[['Team/NOC', 'Gold', 'Silver', 'Bronze', 'Total']][:10]
# Ranking total medals
ranking = df_medals.sort_values(['Total'], ascending=False)
ranking_top10 = ranking[['Team/NOC', 'Total']][:10]
# Gold+
gold_more = df_medals[df_medals['Gold'] == df_medals['Gold'].max()]
gold_more = gold_more[['Team/NOC', 'Gold']].to_string(index=False)
# Silver+
silver_more = df_medals[df_medals['Silver'] == df_medals['Silver'].max()]
silver_more = silver_more[['Team/NOC', 'Silver']].to_string(index=False)
# Bronze+
bronze_more = df_medals[df_medals['Bronze'] == df_medals['Bronze'].max()]
bronze_more = bronze_more[['Team/NOC', 'Bronze']].to_string(index=False)
# Gold-
gold_less = df_medals[df_medals['Gold'] == df_medals['Gold'].min()]
gold_less = gold_less[['Team/NOC', 'Gold']].to_string(index=False)
# Silver-
silver_less = df_medals[df_medals['Silver'] == df_medals['Silver'].min()]
silver_less = silver_less[['Team/NOC', 'Silver']].to_string(index=False)
# Bronze-
bronze_less = df_medals[df_medals['Bronze'] == df_medals['Bronze'].min()]
bronze_less = bronze_less[['Team/NOC', 'Bronze']].to_string(index=False)

# Discipline list
disciplines = df_gender['Discipline'].unique()
qtd_disciplines = (len(disciplines))
# More men than women
disciplines_more_men = df_gender[df_gender['Male'] > df_gender['Female']]
# More women than men
disciplines_more_women = df_gender[df_gender['Female'] > df_gender['Male']]
# Same amount
disciplines_same_amount = df_gender[df_gender['Female'] == df_gender['Male']].to_string(index=False)
# Teams by discipline
teams_list = df_teams['Discipline'].unique()
teams = df_teams.groupby(['Discipline'])['NOC'].value_counts().to_frame('Count')

# Coaches by country
coaches = df_coaches.drop_duplicates(subset="Name")
coaches_country = coaches['NOC'].value_counts()
# More coaches
more_coaches = [coaches_country.index.values[0], coaches_country.values[0]]
# Coaches by discipline
coaches_discipline = coaches['Discipline'].value_counts()
