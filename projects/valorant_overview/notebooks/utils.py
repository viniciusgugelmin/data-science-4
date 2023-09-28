import os


def cprint(text, color, **kwargs):
    color_number = None

    if color == 'blue':
        color_number = 34
    elif color == 'green':
        color_number = 32
    elif color == 'red':
        color_number = 31
    elif color == 'yellow':
        color_number = 33
    elif color == 'purple':
        color_number = 35
    elif color == 'cyan':
        color_number = 36
    else:
        color_number = 37

    print(f'\033[{color_number}m{text}\033[0m', **kwargs)


def show_title():
    cprint('\n------ Análise de dados do meio competitivo de Valorant de 2023 ------', 'cyan')


def show_what_is_the_game():
    cprint('\nO que é Valorant?', 'blue')
    print(
        'Valorant é um jogo de tiro em primeira pessoa desenvolvido pela Riot Games, mesma desenvolvedora de League of '
        'Legends, e foi lançado em 2020. O jogo é gratuito e possui competitivo ranqueado, além de campeonatos '
        'profissionais.')


def show_what_is_an_agent():
    cprint('\nO que é um agente?', 'blue')
    print(
        'Um agente é um personagem com habilidades especiais que podem ser utilizadas durante a partida. Cada agente '
        'possui habilidades únicas e classes diferentes que diferenciam o estilo de jogo de cada um.')


def show_how_many_agents_are_there():
    cprint('\nQuantos agentes existem?', 'blue')
    print('Existem 22 no total, sendo 2 deles lançados em 2023.')


def show_agent_roles():
    cprint('\nQuais são as classes de agentes?', 'blue')
    print(
        'Existem 4 classes de agentes: Duelista, Controlador, Sentinela e Iniciador. Duelistas são agentes que possuem '
        'habilidades que facilitam a troca de tiros e o abate de inimigos. Controladores são agentes que possuem '
        'habilidades que facilitam o controle de território e a visão de inimigos. Sentinela são agentes que possuem '
        'habilidades que facilitam a defesa de território e a proteção de aliados. Iniciadores são agentes que possuem '
        'habilidades que facilitam a obtenção de informações sobre a posição dos inimigos.')


def show_team_player_numbers():
    cprint('\nQuantos jogadores cada time possui?', 'blue')
    print('Cada time possui 6 jogadores, sendo 5 titulares e 1 reserva.')


def show_world_champion():
    cprint('\nQual é a atual equipe campeã mundial de Valorant?', 'blue')
    print(
        'A atual equipe campeã mundial de Valorant é a Evil Geniuses (EG), que venceu o Valorant Champions Los Angeles '
        '2023.')


def show_game_context():
    cprint('\n---- Contextualização ----', 'cyan')

    show_what_is_the_game()
    show_what_is_an_agent()
    show_how_many_agents_are_there()
    show_agent_roles()
    show_team_player_numbers()
    show_world_champion()


def wait_for_type():
    input('')


def menu_control_waiter(options, waiter=False):
    for option in options:
        option()

        if waiter:
            wait_for_type()
        else:
            print()


def menu_control(before_options, options, break_option, break_message):
    while True:
        aux_result = before_options()

        if aux_result is True:
            continue

        if aux_result is False:
            break

        print('\nEscolha uma opção:')

        for key, value in options.items():
            print(f'{key} - {value[0]}')

        print(break_option)

        try:
            option = int(input('Opção: '))
        except KeyboardInterrupt:
            break
        except ValueError:
            break

        if option not in options:
            break

        os.system('cls')

        result = None

        try:
            result = options[option][1](aux_result) if aux_result is not None else options[option][1]()
        except KeyboardInterrupt:
            pass

        if result and isinstance(result, str):
            if len(options[option]) == 3:
                options[option][2](aux_result) if aux_result is not None else options[option][2]()

            print(result)

        if not result or isinstance(result, str) or isinstance(result, dict) and result[
            'dont_send_break_message'] is False:
            try:
                input(break_message)
            except KeyboardInterrupt:
                break

        os.system('cls')
