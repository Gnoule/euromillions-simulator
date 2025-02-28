import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

def generate_euromillions_draw():
    """ Génère un tirage aléatoire d'EuroMillions en tenant compte des probabilités """
    numbers_probabilities = [
        (1, 6.99), (2, 10.96), (3, 8.88), (4, 8.51), (5, 9.26), (6, 9.45), (7, 10.40), (8, 8.51), (9, 9.26), (10, 11.15),
        (11, 10.78), (12, 10.96), (13, 9.83), (14, 9.83), (15, 10.02), (16, 11.72), (17, 10.78), (18, 8.88), (19, 11.34),
        (20, 11.53), (21, 13.23), (22, 6.81), (23, 11.15), (24, 10.40), (25, 10.40), (26, 9.64), (27, 10.40), (28, 9.64),
        (29, 11.34), (30, 8.70), (31, 8.13), (32, 10.02), (33, 10.21), (34, 12.48), (35, 12.85), (36, 9.45), (37, 10.40),
        (38, 9.83), (39, 8.51), (40, 8.88), (41, 9.83), (42, 11.72), (43, 7.56), (44, 10.02), (45, 10.21), (46, 10.40),
        (47, 10.02), (48, 10.21), (49, 8.88), (50, 9.64)
    ]
    
    numbers = random.choices(
        [num for num, prob in numbers_probabilities],
        [prob for num, prob in numbers_probabilities],
        k=5
    )
    stars = random.sample(range(1, 13), 2)  # 2 étoiles parmi 12
    return set(numbers), set(stars)

def check_winnings(player_numbers, player_stars, draw_numbers, draw_stars):
    """ Vérifie le rang de gain d'une grille par rapport à un tirage """
    matched_numbers = len(player_numbers & draw_numbers)
    matched_stars = len(player_stars & draw_stars)
    
    prize_table = {
        (5, 2): (1, "Jackpot"),
        (5, 1): (2, "Très gros gain"),
        (5, 0): (3, "Gros gain"),
        (4, 2): (4, "Bon gain"),
        (4, 1): (5, "Moyen gain"),
        (4, 0): (6, "Petit gain"),
        (3, 2): (7, "Gain moyen"),
        (3, 1): (8, "Gain faible"),
        (3, 0): (9, "Gain très faible"),
        (2, 2): (10, "Petite somme"),
        (2, 1): (11, "Petite somme"),
        (2, 0): (12, "Très petite somme"),
        (1, 2): (13, "Gain minime"),
        (1, 1): (14, "Gain minime"),
        (0, 2): (15, "Gain minime")
    }
    return prize_table.get((matched_numbers, matched_stars), (None, "Perdu"))

def simulate_euromillions(player_numbers, player_stars, num_simulations):
    """ Simule un nombre donné de tirages et affiche les résultats """
    winnings = {rank: 0 for rank in range(1, 16)}
    total_losses = 0
    total_winnings = 0
    ticket_cost = 2.5
    
    prize_amounts = {
        1: 17000000,
        2: 375000,
        3: 40000,
        4: 7500,
        5: 750,
        6: 200,
        7: 125,
        8: 11.26,
        9: 25,
        10: 25,
        11: 15,
        12: 4,
        13: 3.5,
        14: 3.5,
        15: 2.5 
    }
    
    for _ in range(num_simulations):
        draw_numbers, draw_stars = generate_euromillions_draw()
        rank, message = check_winnings(player_numbers, player_stars, draw_numbers, draw_stars)
        if rank:
            winnings[rank] += 1
            total_winnings += prize_amounts[rank]
        else:
            total_losses += 1
    
    total_cost = num_simulations * ticket_cost
    net_profit = total_winnings - total_cost
    
    return net_profit

def run_multiple_simulations(player_numbers, player_stars, num_simulations, num_runs):
    """ Exécute plusieurs simulations et trace un graphique des profits nets """
    net_profits = []
    
    for _ in range(num_runs):
        net_profit = simulate_euromillions(player_numbers, player_stars, num_simulations)
        net_profits.append(net_profit)
    
    # Tracer le graphique des profits nets
    plt.plot(range(1, num_runs + 1), net_profits, marker='o', linestyle='-', color='b')
    
    plt.title('Profits nets après chaque simulation de 5200 tirages')
    plt.xlabel('Simulation')
    plt.ylabel('Profit net (euros)')
    plt.grid(True)
    plt.savefig('net_profits_simulations_10.png')

# Exemple d'utilisation
grille_joueur = {3, 15, 22, 37, 48}  # Choisissez vos 5 numéros
etoiles_joueur = {4, 11}             # Choisissez vos 2 étoiles

# Nombre de parties en 50 ans : 5200
# Nombre de simulations : 1000
run_multiple_simulations(grille_joueur, etoiles_joueur, 5200, 1000)
