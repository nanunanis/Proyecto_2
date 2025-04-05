# Puntaje por ronda
def score (kill, assist, death):
    return (kill * 3) + assist - death


# Cargo un nuevo jugador a la partida
def new_player (round, player, player_data, point):
    player_data[player] = {
        'kills': round[player]['kills'],
        'assists': round[player]['assists'],
        'deaths': 1 if round[player]['deaths'] else 0,
        'MVPs': 0,
        'points': point
    }


# Actualizo las estadisticas del jugador
def update_stats (round, player, player_data, point):
    player_data[player]['kills'] += round[player]['kills']
    player_data[player]['assists'] += round[player]['assists']
    player_data[player]['deaths'] += 1 if round[player]['deaths'] else 0
    player_data[player]['points'] += point


# Busco el mvp de la ronda
def find_mvp (points, best_points, player, mvp_player):
    if points > best_points:
        best_points = points
        mvp_player = player
    return mvp_player, best_points


# Ordeno el diccionario por ronda cargada
def ordenar_ranking (players_data):
    return sorted(players_data.items(), key = lambda x: x[1]['points'], reverse = True) 


# Imprimo los ranking por ronda
def print_ranking (ranking, i):
    if(i<=5):
        print(f"Ranking ronda {i}: ")
    else:
        print(f"Ranking Final: ")
    print(f"{'Jugador':^10} {'Kills':^10} {'Asists':^10} {'Deaths':^10} {'MVPs':^10} {'Puntos':^10}")
    print("-" * 65)
    for player, stats in ranking:
        print(f"{player:^10}{stats['kills']:^12}{stats['assists']:^10}{stats['deaths']:^11}{stats['MVPs']:^12}{stats['points']:^10}")
    print('-' * 65)
    print()