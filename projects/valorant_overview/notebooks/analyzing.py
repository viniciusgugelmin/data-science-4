import pandas as pd
import os
from utils import cprint, show_title, show_game_context, menu_control, menu_control_waiter

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
    df_aux = df.copy()

    def print_base():
        cprint('\n---- Análise inicial dos dados ----', 'cyan')

        cprint('\n-- Base --\n', 'cyan')

        cprint('Quantidade de partidas jogadas em 2023: ', 'blue', end='')
        df_partidas = df_aux.drop_duplicates(subset='id_partida')
        print(df_partidas.shape[0])

    def print_individual_games():
        cprint('Quantidade de jogos individuais jogados em 2023: ', 'blue', end='')
        df_jogos = df_aux.drop_duplicates(subset='id_jogo')
        print(df_jogos.shape[0])

    def print_teams():
        cprint('Quantidade de equipes que jogaram em 2023: ', 'blue', end='')
        df_equipes = df_aux.drop_duplicates(subset='time')
        print(df_equipes.shape[0])

    def print_players():
        cprint('Quantidade de jogadores que jogaram em 2023: ', 'blue', end='')
        df_jogadores = df_aux.drop_duplicates(subset='jogador')
        print(df_jogadores.shape[0])

    def print_not_main_players():
        # ## Quantidade de jogadores reservas não é possível de ser calculada visto que podem ocorrer transferências de
        # jogadores entre equipes durante o ano, e também não há diferença entre jogadores titulares e reservas no dataset
        cprint('Quantidade de jogadores reservas não é possível de ser calculada*', 'yellow')

    def print_agents():
        cprint('Quantidade de agentes que foram utilizados em 2023: ', 'blue', end='')
        df_agentes = df_aux.drop_duplicates(subset='agente')
        print(df_agentes.shape[0])

    def print_most_played_team():
        cprint('-- Times --', 'cyan')

        cprint('\nTime com mais jogos jogados em 2023, junto com a quantidade de jogos: ', 'blue', end='')
        df_jogos = df_aux.groupby(['time', 'id_jogo']).sum().reset_index().groupby('time').size().reset_index(
            name='count').sort_values(by='count', ascending=False)
        print(df_jogos.iloc[0, 0], df_jogos.iloc[0, 1], sep=' - ')

    def print_less_played_team():
        cprint('Times com menos jogos jogados em 2023, junto com a quantidade de jogos: ', 'blue', end='')
        df_jogos = df_aux.groupby(['time', 'id_jogo']).sum().reset_index().groupby('time').size().reset_index(
            name='count').sort_values(by='count', ascending=True)
        df_jogos = df_jogos.sort_values(by='count', ascending=True)
        df_jogos = df_jogos[df_jogos['count'] == df_jogos.iloc[0, 1]]

        for i in range(df_jogos.shape[0]):
            print(df_jogos.iloc[i, 0], df_jogos.iloc[i, 1], sep=' - ', end='')

            if i != df_jogos.shape[0] - 1:
                print(' | ', end='')
            else:
                print('')

    def print_most_victorious_team():
        # ## Time com mais vitórias e com menos vitórias não serão dados relevantes para a análise pelo fato de o competitivo
        # de Valorant se basear muito em chaves de eliminação, onde o time que perde é eliminado do torneio, e o time que
        # ganha continua no torneio, e o time que ganha o torneio é o campeão
        cprint('Time com mais vitórias e menos vitórias não serão dados relevantes para a análise*', 'yellow')

    def print_most_killer_player():
        cprint('-- Jogadores --', 'cyan')

        cprint('\nJogador com mais abates em 2023, junto com a quantidade de abates e o time que ele joga: ', 'blue',
               end='')
        df_abates = df_aux.groupby('jogador').sum().reset_index().sort_values(by='abates', ascending=False)
        jogador_mais_abates_time = df_aux[df_aux['jogador'] == df_abates.iloc[0, 0]]['time'].iloc[0]
        print(df_abates['jogador'].iloc[0], df_abates['abates'].iloc[0], jogador_mais_abates_time,
              sep=' - ')

    def print_most_killer_player_mean():
        cprint('Média de abates do jogador com mais abates em 2023: ', 'blue', end='')
        df_abates = df_aux.groupby('jogador').sum().reset_index().sort_values(by='abates', ascending=False)
        df_abates['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
        df_abates['media_abates'] = df_abates['abates'] / df_abates['jogos']
        df_abates['media_abates'] = df_abates['media_abates'].astype(int)
        print(df_abates['media_abates'].iloc[0])

    def print_less_killer_player():
        cprint('Jogador com menos abates em 2023, junto com a quantidade de abates e o time que ele joga: ', 'blue',
               end='')
        df_abates = df_aux.groupby('jogador').sum().reset_index().sort_values(by='abates', ascending=False)
        df_abates['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
        df_abates['media_abates'] = df_abates['abates'] / df_abates['jogos']
        df_abates['media_abates'] = df_abates['media_abates'].astype(int)
        df_abates = df_abates.sort_values(by='abates', ascending=True)
        jogador_menos_abates_time = df_aux[df_aux['jogador'] == df_abates.iloc[0, 0]]['time'].iloc[0]
        print(df_abates['jogador'].iloc[0], df_abates['abates'].iloc[0], jogador_menos_abates_time,
              sep=' - ')

    def print_less_killer_player_mean():
        cprint('Média de abates do jogador com menos abates em 2023: ', 'blue', end='')
        df_abates = df_aux.groupby('jogador').sum().reset_index().sort_values(by='abates', ascending=False)
        df_abates['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
        df_abates['media_abates'] = df_abates['abates'] / df_abates['jogos']
        df_abates['media_abates'] = df_abates['media_abates'].astype(int)
        df_abates = df_abates.sort_values(by='abates', ascending=True)
        print(df_abates['media_abates'].iloc[0])

    def print_most_killed_player():
        cprint('Jogador com mais mortes em 2023, junto com a quantidade de mortes e o time que ele joga: ', 'blue',
               end='')
        df_mortes = df_aux.groupby('jogador').sum().reset_index().sort_values(by='mortes', ascending=False)
        jogador_mais_mortes_time = df_aux[df_aux['jogador'] == df_mortes.iloc[0, 0]]['time'].iloc[0]
        print(df_mortes['jogador'].iloc[0], df_mortes['mortes'].iloc[0], jogador_mais_mortes_time,
              sep=' - ')

    def print_most_killed_player_mean():
        cprint('Média de mortes do jogador com mais mortes em 2023: ', 'blue', end='')
        df_mortes = df_aux.groupby('jogador').sum().reset_index().sort_values(by='mortes', ascending=False)
        df_mortes['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
        df_mortes['media_mortes'] = df_mortes['mortes'] / df_mortes['jogos']
        df_mortes['media_mortes'] = df_mortes['media_mortes'].astype(int)
        print(df_mortes['media_mortes'].iloc[0])

    def print_less_killed_player():
        cprint('Jogador com menos mortes em 2023, junto com a quantidade de mortes e o time que ele joga: ', 'blue',
               end='')
        df_mortes = df_aux.groupby('jogador').sum().reset_index().sort_values(by='mortes', ascending=False)
        df_mortes['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
        df_mortes['media_mortes'] = df_mortes['mortes'] / df_mortes['jogos']
        df_mortes['media_mortes'] = df_mortes['media_mortes'].astype(int)
        df_mortes = df_mortes.sort_values(by='mortes', ascending=True)
        jogador_menos_mortes_time = df_aux[df_aux['jogador'] == df_mortes.iloc[0, 0]]['time'].iloc[0]
        print(df_mortes['jogador'].iloc[0], df_mortes['mortes'].iloc[0], jogador_menos_mortes_time,
              sep=' - ')

    def print_less_killed_player_mean():
        cprint('Média de mortes do jogador com menos mortes em 2023: ', 'blue', end='')
        df_mortes = df_aux.groupby('jogador').sum().reset_index().sort_values(by='mortes', ascending=True)
        df_mortes['jogos'] = df_aux.groupby('jogador').size().reset_index(name='count')['count']
        df_mortes['media_mortes'] = df_mortes['mortes'] / df_mortes['jogos']
        df_mortes['media_mortes'] = df_mortes['media_mortes'].astype(int)
        print(df_mortes['media_mortes'].iloc[0])

    def print_most_hs_player():
        cprint('Jogador com maior taxa de headshots em 2023, junto com a taxa de headshots e o time que ele joga: ',
               'blue',
               end='')
        df_headshots = df_aux.groupby('jogador').sum().reset_index().sort_values(by='hs_percentual', ascending=False)
        df_headshots['hs_percentual'] = df_headshots['hs_percentual'].astype(int) / \
                                        df_aux.groupby('jogador').size().reset_index(name='count')['count']
        jogador_maior_hs_time = df_aux[df_aux['jogador'] == df_headshots.iloc[0, 0]]['time'].iloc[0]
        print(df_headshots['jogador'].iloc[0], df_headshots['hs_percentual'].astype(int).iloc[0].astype(str) + '%',
              jogador_maior_hs_time, sep=' - ')

    def print_most_hs_player_mean():
        cprint('Jogador com menor taxa de headshots em 2023, junto com a taxa de headshots e o time que ele joga: ',
               'blue',
               end='')
        df_headshots = df_aux.groupby('jogador').sum().reset_index().sort_values(by='hs_percentual', ascending=False)
        df_headshots['hs_percentual'] = df_headshots['hs_percentual'].astype(int) / \
                                        df_aux.groupby('jogador').size().reset_index(name='count')['count']
        df_headshots = df_headshots.sort_values(by='hs_percentual', ascending=True)
        jogador_menor_hs_time = df_aux[df_aux['jogador'] == df_headshots.iloc[0, 0]]['time'].iloc[0]
        print(df_headshots['jogador'].iloc[0], df_headshots['hs_percentual'].astype(int).iloc[0].astype(str) + '%',
              jogador_menor_hs_time, sep=' - ')

    options = [
        print_base,
        print_individual_games,
        print_teams,
        print_players,
        print_not_main_players,
        print_agents,
        print_most_played_team,
        print_less_played_team,
        print_most_victorious_team,
        print_most_killer_player,
        print_most_killer_player_mean,
        print_less_killer_player,
        print_less_killer_player_mean,
        print_most_killed_player,
        print_most_killed_player_mean,
        print_less_killed_player,
        print_less_killed_player_mean,
        print_most_hs_player,
        print_most_hs_player_mean
    ]

    menu_control_waiter(options)


def team_names():
    df_aux = df.copy()

    cprint('\n- Nomes de todos os times que jogaram em 2023 -\n', 'cyan')

    teams = df_aux['time'].sort_values().unique()
    teams = ', '.join(teams)
    print(teams)


def team_more_maps_played(team):
    df_aux = df.copy()

    cprint('\n- Time que mais jogou mapas em 2023 -\n', 'cyan')
    df_team = df_aux[df_aux['time'] == team]
    df_team = df_team.groupby(['id_jogo', 'time', 'mapa']).size().reset_index(name='count')
    df_team['count'] = 1
    df_team = df_team.groupby('mapa').sum().reset_index().sort_values(by='count', ascending=False)
    team_map = df_team['mapa'].iloc[0]
    number_plays = df_team['count'].iloc[0]
    max_number_of_maps = df_team['count'].sum()
    percent = (number_plays / max_number_of_maps) * 100

    return f'{team_map} ({number_plays}/{max_number_of_maps}) - {percent:.2f}%'


def team_more_map_win_percent(team):
    df_aux = df.copy()

    team_df = df_aux[df_aux['time'] == team]
    team_df = team_df[team_df['ganhou_perdeu'] == True]
    team_df = team_df.groupby(['id_jogo', 'time', 'mapa']).size().reset_index(name='count')
    team_df['count'] = 1
    team_df = team_df['mapa'].value_counts().reset_index()
    team_df.columns = ['mapa', 'vitorias']
    team_df_aux = df_aux[df_aux['time'] == team]
    team_df_aux = team_df_aux.groupby(['id_jogo', 'time', 'mapa']).size().reset_index(name='count')
    team_df_aux['count'] = 1
    team_df_aux = team_df_aux['mapa'].value_counts().reset_index()
    team_df['total'] = team_df['mapa'].map(team_df_aux.set_index('mapa')['count'])
    team_df['percentual'] = (team_df['vitorias'] / team_df['total']) * 100
    team_df = team_df.sort_values(by='percentual', ascending=False)

    string_to_return = ''

    for index, row in team_df.iterrows():
        string_to_return += f'{row["mapa"]} ({row["vitorias"]}/{row["total"]}) - {row["percentual"]:.2f}%\n'

    return string_to_return


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

    def more_maps_win_percent_print(team):
        cprint('\n- Estatísticas de um time em 2023 -\n', 'cyan')
        cprint(f'Mapas com maior taxa de vitória do(a) {team} em 2023: ', 'blue')

    options = {
        1: [
            'Mapa mais jogado',
            team_more_maps_played,
            more_maps_played_print,
        ],
        2: [
            'Mapas com maior taxa de vitória',
            team_more_map_win_percent,
            more_maps_win_percent_print,
        ],
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
    # print(df.groupby(['time', 'id_jogo']).sum().reset_index().groupby('time').size().sort_values(ascending=False))
