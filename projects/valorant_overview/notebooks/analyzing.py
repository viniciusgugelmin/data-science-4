import pandas as pd
import os
from libs import cprint

cprint('\n------ Análise de dados do meio competitivo de Valorant de 2023 ------', 'cyan')

# Contextualização

cprint('\n---- Contextualização ----', 'cyan')

cprint('\nO que é Valorant?', 'blue')
print(
    'Valorant é um jogo de tiro em primeira pessoa desenvolvido pela Riot Games, mesma desenvolvedora de League of '
    'Legends, e foi lançado em 2020. O jogo é gratuito e possui competitivo ranqueado, além de campeonatos '
    'profissionais.')

cprint('\nO que é um agente?', 'blue')
print(
    'Um agente é um personagem com habilidades especiais que podem ser utilizadas durante a partida. Cada agente '
    'possui habilidades únicas e classes diferentes que diferenciam o estilo de jogo de cada um.')

cprint('\nQuais são as classes de agentes?', 'blue')
print(
    'Existem 4 classes de agentes: Duelista, Controlador, Sentinela e Iniciador. Duelistas são agentes que possuem '
    'habilidades que facilitam a troca de tiros e o abate de inimigos. Controladores são agentes que possuem '
    'habilidades que facilitam o controle de território e a visão de inimigos. Sentinela são agentes que possuem '
    'habilidades que facilitam a defesa de território e a proteção de aliados. Iniciadores são agentes que possuem '
    'habilidades que facilitam a obtenção de informações sobre a posição dos inimigos.')

cprint('\nQuantos agentes existem?', 'blue')
print('Existem 22 no total, sendo 2 deles lançados em 2023.')

cprint('\nQuantos jogadores cada time possui?', 'blue')
print('Cada time possui 6 jogadores, sendo 5 titulares e 1 reserva.')

cprint('\nQual é a atual equipe campeã mundial de Valorant?', 'blue')
print('A atual equipe campeã mundial de Valorant é a Evil Geniuses (EG), que venceu o Valorant Champions Los Angeles '
      '2023.')

# Configuração de variáveis para carregamento de paths

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = dir_path + '\\..\\data'

# Carregamento dos datasets

## 1 - Dados de resultados obtidos de todas as partidas de todos os torneios de valorant de 2023

df_url = data_path + '\\dataset_clean.csv'
df = pd.read_csv(df_url, sep=',', encoding='utf-8')

## 2 - Dados obtidos através de scrapping, mostrando o montante adquirido por cada jogador de Valorant em 2023

df2_url = data_path + '\\dataset2_clean.csv'
df2 = pd.read_csv(df2_url, sep=',', encoding='utf-8')

# Análise inicial dos dados

cprint('\n---- Análise inicial dos dados ----', 'cyan')

df_aux = df.copy()

cprint('\n-- Base --', 'cyan')

cprint('\nQuantidade de partidas jogadas em 2023: ', 'blue', end='')
df_partidas = df_aux.drop_duplicates(subset='id_partida')
print(df_partidas.shape[0])

cprint('\nQuantidade de jogos individuais jogados em 2023: ', 'blue', end='')
df_jogos = df_aux.drop_duplicates(subset='id_jogo')
print(df_jogos.shape[0])

cprint('\nQuantidade de equipes que jogaram em 2023: ', 'blue', end='')
df_equipes = df_aux.drop_duplicates(subset='time')
print(df_equipes.shape[0])

cprint('\nQuantidade de jogadores que jogaram em 2023: ', 'blue', end='')
df_jogadores = df_aux.drop_duplicates(subset='jogador')
print(df_jogadores.shape[0])

# ## Quantidade de jogadores reservas não é possível de ser calculada visto que podem ocorrer transferências de
# jogadores entre equipes durante o ano, e também não há diferença entre jogadores titulares e reservas no dataset
cprint('\nQuantidade de jogadores reservas não é possível de ser calculada*', 'yellow')

cprint('\nQuantidade de agentes que foram utilizados em 2023: ', 'blue', end='')
df_agentes = df_aux.drop_duplicates(subset='agente')
print(df_agentes.shape[0])

cprint('\n-- Times --', 'cyan')

cprint('\nTime com mais jogos jogados em 2023, junto com a quantidade de jogos: ', 'blue', end='')
df_jogos = df_aux.groupby('time').size().reset_index(name='count').sort_values(by='count', ascending=False)
print(df_jogos.iloc[0, 0], df_jogos.iloc[0, 1], sep=' - ')

cprint('\nTimes com menos jogos jogados em 2023, junto com a quantidade de jogos: ', 'blue', end='')
df_jogos = df_jogos.sort_values(by='count', ascending=True)
time_menos_jogos = df_jogos.iloc[0, 0]
df_jogos = df_jogos[df_jogos['count'] == df_jogos.iloc[0, 1]]

for i in range(df_jogos.shape[0]):
    print(df_jogos.iloc[i, 0], df_jogos.iloc[i, 1], sep=' - ', end='')

    if i != df_jogos.shape[0] - 1:
        print(' | ', end='')
    else:
        print('')

# ## Time com mais vitórias e com menos vitórias não serão dados relevantes para a análise pelo fato de o competitivo
# de Valorant se basear muito em chaves de eliminação, onde o time que perde é eliminado do torneio, e o time que
# ganha continua no torneio, e o time que ganha o torneio é o campeão
cprint('\nTime com mais vitórias e menos vitórias não serão dados relevantes para a análise*', 'yellow')

cprint('\n-- Jogadores --', 'cyan')

cprint('\nJogador com mais abates em 2023, junto com a quantidade de abates e o time que ele joga: ', 'blue', end='')
df_abates = df_aux.groupby('jogador').sum().reset_index().sort_values(by='abates', ascending=False)
jogador_mais_abates_time = df_aux[df_aux['jogador'] == df_abates.iloc[0, 0]]['time'].iloc[0]
print(df_abates['jogador'].iloc[0], df_abates['abates'].iloc[0], jogador_mais_abates_time,
      sep=' - ')

cprint('\nMédia de abates do jogador com mais abates em 2023: ', 'blue', end='')
df_abates['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
df_abates['media_abates'] = df_abates['abates'] / df_abates['jogos']
df_abates['media_abates'] = df_abates['media_abates'].astype(int)
print(df_abates['media_abates'].iloc[0])

cprint('\nJogador com menos abates em 2023, junto com a quantidade de abates e o time que ele joga: ', 'blue', end='')
df_abates = df_abates.sort_values(by='abates', ascending=True)
jogador_menos_abates_time = df_aux[df_aux['jogador'] == df_abates.iloc[0, 0]]['time'].iloc[0]
print(df_abates['jogador'].iloc[0], df_abates['abates'].iloc[0], jogador_menos_abates_time,
        sep=' - ')

cprint('\nMédia de abates do jogador com menos abates em 2023: ', 'blue', end='')
print(df_abates['media_abates'].iloc[0])

cprint('\nJogador com mais mortes em 2023, junto com a quantidade de mortes e o time que ele joga: ', 'blue', end='')
df_mortes = df_aux.groupby('jogador').sum().reset_index().sort_values(by='mortes', ascending=False)
jogador_mais_mortes_time = df_aux[df_aux['jogador'] == df_mortes.iloc[0, 0]]['time'].iloc[0]
print(df_mortes['jogador'].iloc[0], df_mortes['mortes'].iloc[0], jogador_mais_mortes_time,
        sep=' - ')

cprint('\nMédia de mortes do jogador com mais mortes em 2023: ', 'blue', end='')
df_mortes['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
df_mortes['media_mortes'] = df_mortes['mortes'] / df_mortes['jogos']
df_mortes['media_mortes'] = df_mortes['media_mortes'].astype(int)
print(df_mortes['media_mortes'].iloc[0])

cprint('\nJogador com menos mortes em 2023, junto com a quantidade de mortes e o time que ele joga: ', 'blue', end='')
df_mortes = df_mortes.sort_values(by='mortes', ascending=True)
jogador_menos_mortes_time = df_aux[df_aux['jogador'] == df_mortes.iloc[0, 0]]['time'].iloc[0]
print(df_mortes['jogador'].iloc[0], df_mortes['mortes'].iloc[0], jogador_menos_mortes_time,
        sep=' - ')

cprint('\nMédia de mortes do jogador com menos mortes em 2023: ', 'blue', end='')
print(df_mortes['media_mortes'].iloc[0])

cprint('\nJogador com maior taxa de headshots em 2023, junto com a taxa de headshots e o time que ele joga: ', 'blue', end='')
df_headshots = df_aux.groupby('jogador').sum().reset_index().sort_values(by='hs_percentual', ascending=False)
df_headshots['hs_percentual'] = df_headshots['hs_percentual'].astype(int) / df_aux.groupby('jogador').size().reset_index(name='count')['count']
jogador_maior_hs_time = df_aux[df_aux['jogador'] == df_headshots.iloc[0, 0]]['time'].iloc[0]
print(df_headshots['jogador'].iloc[0], df_headshots['hs_percentual'].astype(int).iloc[0].astype(str) + '%', jogador_maior_hs_time, sep=' - ')

cprint('\nJogador com menor taxa de headshots em 2023, junto com a taxa de headshots e o time que ele joga: ', 'blue', end='')
df_headshots = df_headshots.sort_values(by='hs_percentual', ascending=True)
jogador_menor_hs_time = df_aux[df_aux['jogador'] == df_headshots.iloc[0, 0]]['time'].iloc[0]
print(df_headshots['jogador'].iloc[0], df_headshots['hs_percentual'].astype(int).iloc[0].astype(str) + '%', jogador_menor_hs_time, sep=' - ')



