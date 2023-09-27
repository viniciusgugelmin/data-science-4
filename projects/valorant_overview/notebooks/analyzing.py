import pandas as pd
import os
from utils import cprint, show_title, show_game_context, wait_for_type, menu_control

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


def show_initial_analysis():
    cprint('\n---- Análise inicial dos dados ----', 'cyan')

    df_aux = df.copy()

    cprint('\n-- Base --', 'cyan')

    cprint('Quantidade de partidas jogadas em 2023: ', 'blue', end='')
    df_partidas = df_aux.drop_duplicates(subset='id_partida')
    print(df_partidas.shape[0])

    wait_for_type()

    cprint('Quantidade de jogos individuais jogados em 2023: ', 'blue', end='')
    df_jogos = df_aux.drop_duplicates(subset='id_jogo')
    print(df_jogos.shape[0])

    wait_for_type()

    cprint('Quantidade de equipes que jogaram em 2023: ', 'blue', end='')
    df_equipes = df_aux.drop_duplicates(subset='time')
    print(df_equipes.shape[0])

    wait_for_type()

    cprint('Quantidade de jogadores que jogaram em 2023: ', 'blue', end='')
    df_jogadores = df_aux.drop_duplicates(subset='jogador')
    print(df_jogadores.shape[0])

    wait_for_type()

    # ## Quantidade de jogadores reservas não é possível de ser calculada visto que podem ocorrer transferências de
    # jogadores entre equipes durante o ano, e também não há diferença entre jogadores titulares e reservas no dataset
    cprint('Quantidade de jogadores reservas não é possível de ser calculada*', 'yellow')

    wait_for_type()

    cprint('Quantidade de agentes que foram utilizados em 2023: ', 'blue', end='')
    df_agentes = df_aux.drop_duplicates(subset='agente')
    print(df_agentes.shape[0])

    wait_for_type()

    cprint('-- Times --', 'cyan')

    cprint('\nTime com mais jogos jogados em 2023, junto com a quantidade de jogos: ', 'blue', end='')
    df_jogos = df_aux.groupby('time').size().reset_index(name='count').sort_values(by='count', ascending=False)
    print(df_jogos.iloc[0, 0], df_jogos.iloc[0, 1], sep=' - ')

    wait_for_type()

    cprint('Times com menos jogos jogados em 2023, junto com a quantidade de jogos: ', 'blue', end='')
    df_jogos = df_jogos.sort_values(by='count', ascending=True)
    time_menos_jogos = df_jogos.iloc[0, 0]
    df_jogos = df_jogos[df_jogos['count'] == df_jogos.iloc[0, 1]]

    for i in range(df_jogos.shape[0]):
        print(df_jogos.iloc[i, 0], df_jogos.iloc[i, 1], sep=' - ', end='')

        if i != df_jogos.shape[0] - 1:
            print(' | ', end='')
        else:
            print('')

    wait_for_type()

    # ## Time com mais vitórias e com menos vitórias não serão dados relevantes para a análise pelo fato de o competitivo
    # de Valorant se basear muito em chaves de eliminação, onde o time que perde é eliminado do torneio, e o time que
    # ganha continua no torneio, e o time que ganha o torneio é o campeão
    cprint('Time com mais vitórias e menos vitórias não serão dados relevantes para a análise*', 'yellow')

    wait_for_type()

    cprint('-- Jogadores --', 'cyan')

    cprint('\nJogador com mais abates em 2023, junto com a quantidade de abates e o time que ele joga: ', 'blue',
           end='')
    df_abates = df_aux.groupby('jogador').sum().reset_index().sort_values(by='abates', ascending=False)
    jogador_mais_abates_time = df_aux[df_aux['jogador'] == df_abates.iloc[0, 0]]['time'].iloc[0]
    print(df_abates['jogador'].iloc[0], df_abates['abates'].iloc[0], jogador_mais_abates_time,
          sep=' - ')

    wait_for_type()

    cprint('Média de abates do jogador com mais abates em 2023: ', 'blue', end='')
    df_abates['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
    df_abates['media_abates'] = df_abates['abates'] / df_abates['jogos']
    df_abates['media_abates'] = df_abates['media_abates'].astype(int)
    print(df_abates['media_abates'].iloc[0])

    wait_for_type()

    cprint('Jogador com menos abates em 2023, junto com a quantidade de abates e o time que ele joga: ', 'blue',
           end='')
    df_abates = df_abates.sort_values(by='abates', ascending=True)
    jogador_menos_abates_time = df_aux[df_aux['jogador'] == df_abates.iloc[0, 0]]['time'].iloc[0]
    print(df_abates['jogador'].iloc[0], df_abates['abates'].iloc[0], jogador_menos_abates_time,
          sep=' - ')

    wait_for_type()

    cprint('Média de abates do jogador com menos abates em 2023: ', 'blue', end='')
    print(df_abates['media_abates'].iloc[0])

    wait_for_type()

    cprint('Jogador com mais mortes em 2023, junto com a quantidade de mortes e o time que ele joga: ', 'blue',
           end='')
    df_mortes = df_aux.groupby('jogador').sum().reset_index().sort_values(by='mortes', ascending=False)
    jogador_mais_mortes_time = df_aux[df_aux['jogador'] == df_mortes.iloc[0, 0]]['time'].iloc[0]
    print(df_mortes['jogador'].iloc[0], df_mortes['mortes'].iloc[0], jogador_mais_mortes_time,
          sep=' - ')

    wait_for_type()

    cprint('Média de mortes do jogador com mais mortes em 2023: ', 'blue', end='')
    df_mortes['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
    df_mortes['media_mortes'] = df_mortes['mortes'] / df_mortes['jogos']
    df_mortes['media_mortes'] = df_mortes['media_mortes'].astype(int)
    print(df_mortes['media_mortes'].iloc[0])

    wait_for_type()

    cprint('Jogador com menos mortes em 2023, junto com a quantidade de mortes e o time que ele joga: ', 'blue',
           end='')
    df_mortes = df_mortes.sort_values(by='mortes', ascending=True)
    jogador_menos_mortes_time = df_aux[df_aux['jogador'] == df_mortes.iloc[0, 0]]['time'].iloc[0]
    print(df_mortes['jogador'].iloc[0], df_mortes['mortes'].iloc[0], jogador_menos_mortes_time,
          sep=' - ')

    wait_for_type()

    cprint('Média de mortes do jogador com menos mortes em 2023: ', 'blue', end='')
    print(df_mortes['media_mortes'].iloc[0])

    wait_for_type()

    cprint('Jogador com maior taxa de headshots em 2023, junto com a taxa de headshots e o time que ele joga: ',
           'blue',
           end='')
    df_headshots = df_aux.groupby('jogador').sum().reset_index().sort_values(by='hs_percentual', ascending=False)
    df_headshots['hs_percentual'] = df_headshots['hs_percentual'].astype(int) / \
                                    df_aux.groupby('jogador').size().reset_index(name='count')['count']
    jogador_maior_hs_time = df_aux[df_aux['jogador'] == df_headshots.iloc[0, 0]]['time'].iloc[0]
    print(df_headshots['jogador'].iloc[0], df_headshots['hs_percentual'].astype(int).iloc[0].astype(str) + '%',
          jogador_maior_hs_time, sep=' - ')

    wait_for_type()

    cprint('Jogador com menor taxa de headshots em 2023, junto com a taxa de headshots e o time que ele joga: ',
           'blue',
           end='')
    df_headshots = df_headshots.sort_values(by='hs_percentual', ascending=True)
    jogador_menor_hs_time = df_aux[df_aux['jogador'] == df_headshots.iloc[0, 0]]['time'].iloc[0]
    print(df_headshots['jogador'].iloc[0], df_headshots['hs_percentual'].astype(int).iloc[0].astype(str) + '%',
          jogador_menor_hs_time, sep=' - ')


def team_names():
    df_aux = df.copy()

    cprint('\n- Nomes de todos os times que jogaram em 2023 -\n', 'cyan')

    teams = df_aux['time'].sort_values().unique()
    teams = ', '.join(teams)
    print(teams)


def team_more_maps_played(team):
    df_aux = df.copy()

    _team = df_aux[df_aux['time'] == team]['mapa'].value_counts().index[0]
    number = df_aux[df_aux['time'] == team]['mapa'].value_counts().values[0]
    max_number = df_aux[df_aux['time'] == team].shape[0]

    return f'{_team} ({number}/{max_number})'


def team_stats():
    df_aux = df.copy()

    def before_options():
        cprint('\n- Estatísticas de um time em 2023 -\n', 'cyan')
        cprint('Escolha um time (ou pressione apenas ENTER para voltar): ', 'blue', end='')
        team = input()

        if team == '':
            return False

        if team not in df_aux['time'].unique():
            cprint('\nTime não encontrado!\n', 'red')
            input('Digite qualquer outra coisa para tentar novamente')
            os.system('cls')
            return True

        return team

    def more_maps_played_print(team):
        cprint('\n- Estatísticas de um time em 2023 -\n', 'cyan')
        cprint(f'Mapa mais jogado pelo(a) {team} em 2023: ', 'blue', end='')

    options = {
        1: [
            'Mapa mais jogado',
            team_more_maps_played,
            more_maps_played_print,
        ]
    }

    menu_control(before_options, options, break_option='Digite qualquer outra coisa para voltar',
                 break_message='\nDigite qualquer tecla para voltar...')


def team_analysis():
    def before_options():
        cprint('\n-- Análise de times --', 'cyan')

    options = {
        1: [
            'Nome de todos os times',
            team_names
        ],
        2: [
            'Estatísticas de um time',
            team_stats
        ]
    }

    menu_control(before_options, options, break_option='Digite qualquer outra coisa para voltar',
                 break_message='\nDigite qualquer tecla para voltar...')

    return {
        'dont_send_break_message': True
    }


def dynamic_analysis():
    def before_options():
        cprint('\n---- Análise dinâmica ----', 'cyan')

    options = {
        1: [
            'Análise de times',
            team_analysis
        ]
    }

    menu_control(before_options, options, break_option='Digite qualquer outra coisa para voltar ao menu',
                 break_message='\nDigite qualquer tecla para voltar...')

    return {
        'dont_send_break_message': True
    }


def main():
    def before_options():
        show_title()

        cprint('\n-- Menu --', 'cyan')

    options = {
        1: [
            'Contextualização',
            show_game_context
        ],
        2: [
            'Análise inicial',
            show_initial_analysis
        ],
        3: [
            'Análise dinâmica',
            dynamic_analysis
        ]
    }

    menu_control(before_options, options, break_option='Digite qualquer outra coisa para sair',
                 break_message='\nDigite qualquer tecla para voltar ao menu...')


if __name__ == '__main__':
    main()
