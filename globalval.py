import math
class globalval:
    ga = 0
    pb64 = 18.7 - 9.74 * (math.exp(1.55125 * ga / 10) - 1)
    pb74 = 15.628 - 9.74 * (math.exp(9.8485 * ga / 10) - 1) / 137.88
    pb84 = 38.63 - 36.84 * (math.exp(0.49475 * ga / 10) - 1)
    leadlossage = 0
    monte_trials = 100
# print(globalval.monte_trials)