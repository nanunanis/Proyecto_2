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