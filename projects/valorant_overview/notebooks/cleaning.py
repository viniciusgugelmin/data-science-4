import pandas as pd
import os

# Configuração de variáveis para carregamento de paths

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = dir_path + '\\..\\data'

# Carregamento dos datasets

## 1 - Dados de resultados obtidos de todas as partidas de todos os torneios de valorant de 2023
df_url = data_path + '\\dataset.csv'
df = pd.read_csv(df_url, sep=',', encoding='utf-8')

## 2 - Dados obtidos através de scrapping, mostrando o montante adquirido por cada jogador de Valorant em 2023
df2_url = data_path + '\\dataset2.csv'
df2 = pd.read_csv(df2_url, sep=',', encoding='utf-8')

# Limpeza do dataset 1

## Remoção de colunas desnecessárias
columns_to_drop = ['Unnamed: 0', 'player_id']
df.drop(columns_to_drop, axis=1, inplace=True)

## Renomeação de colunas
columns_to_rename = {
    'match_id': 'id_partida',
    'game_id': 'id_jogo',
    'team': 'time',
    'score_team': 'pontos_time',
    'opponent': 'oponente',
    'score_opp': 'pontos_oponente',
    'win_lose': 'ganhou_perdeu',
    'map': 'mapa',
    'map_pick': 'escolha_mapa',
    'player': 'jogador',
    'agent': 'agente',
    'rating': 'kda',
    'acs': 'pontuacao',
    'kill': 'abates',
    'death': 'mortes',
    'assist': 'assistencias',
    'kast%': 'kast_percentual',
    'adr': 'media_dano',
    'hs%': 'hs_percentual',
    'fk': 'primeiro_abate',
    'fd': 'primeira_morte',
}
df.rename(columns_to_rename, axis=1, inplace=True)

## Mudança de valores para facilitar a análise
df['ganhou_perdeu'] = df['ganhou_perdeu'].replace('opponent win', False)
df['ganhou_perdeu'] = df['ganhou_perdeu'].replace('team win', True)

df['escolha_mapa'] = df['escolha_mapa'].replace('opponent pick', False)
df['escolha_mapa'] = df['escolha_mapa'].replace('team pick', True)

df['kda'] = df['kda'].replace('\xa0', None)
df['kda'] = df['kda'].astype(float)

df['kast_percentual'] = df['kast_percentual'].replace('\xa0', None)
df['kast_percentual'] = df['kast_percentual'].str.replace('%', '')
df['kast_percentual'] = df['kast_percentual'].fillna(0).astype(int)

df['pontuacao'] = df['pontuacao'].replace('\xa0', None)
df['pontuacao'] = df['pontuacao'].fillna(0).astype(int)

df['media_dano'] = df['media_dano'].replace('\xa0', None)
df['media_dano'] = df['media_dano'].fillna(0).astype(int)

df['hs_percentual'] = df['hs_percentual'].replace('\xa0', None)
df['hs_percentual'] = df['hs_percentual'].str.replace('%', '')
df['hs_percentual'] = df['hs_percentual'].fillna(0).astype(int)

df['primeiro_abate'] = df['primeiro_abate'].replace('\xa0', None)
df['primeiro_abate'] = df['primeiro_abate'].fillna(0).astype(int)

df['primeira_morte'] = df['primeira_morte'].replace('\xa0', None)
df['primeira_morte'] = df['primeira_morte'].fillna(0).astype(int)

## Geração de csv limpo

df.to_csv(data_path + '\\dataset_clean.csv', sep=',', encoding='utf-8', index=False)

# Limpeza do dataset 2

## TODO
