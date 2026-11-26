from itertools import product

P_Rain = {
    True: 0.2,
    False: 0.8
}

P_Sprinkler = {
    True: {True: 0.01, False: 0.4},
    False: {True: 0.99, False: 0.6}
}

P_WetGrass = {
    (True, True): 0.99,
    (True, False): 0.90,
    (False, True): 0.80,
    (False, False): 0.01
}

def probability_wet_grass():
    total = 0

    for rain, sprinkler in product([True, False], repeat=2):
        p_rain = P_Rain[rain]
        p_sprinkler = P_Sprinkler[rain][sprinkler]
        p_wet = P_WetGrass[(rain, sprinkler)]

        total += p_rain * p_sprinkler * p_wet

    return total

result = probability_wet_grass()

print("Bayesian Network")
print("Probability of Rain:", P_Rain[True])
print("Probability of Wet Grass:", round(result, 4))
