from numpy.random import randint
from numpy.random import rand


def selection(population, scores, k=3):                     # reprodukcja turniejowa
    selection_ix = randint(len(population))                 # jeżeli nie przekazujemy do funkcji trzeciego
    for ix in randint(0, len(population), k - 1):           # argumentu to defaultowo wylosuje trzech
        if scores[ix] > scores[selection_ix]:               # osobników i zwróci najlepszego z nich
            selection_ix = ix
        return population[selection_ix]


def crossover(parent1, parent2, r_crossover):               # krzyżowanie dwójki rodziców
    child1, child2 = parent1.copy(), parent2.copy()         # zwraca dwójkę dzieci
    if rand() < r_crossover:                                # krzyżowanie jeśli spełniony
        cross_point = randint(1, len(parent1) - 2)          # warunek związany z współczynnikiem krzyżowania
        child1 = parent1[:cross_point] + parent2[cross_point:]
        child2 = parent2[:cross_point] + parent1[cross_point:]
    return [child1, child2]


def mutation(bit_vector, r_mutation):                       # mutowanie wektora jeśli spełniony
    for i in range(len(bit_vector)):                        # warunek związany z wpółczynnikiem mutowania
        if rand() < r_mutation:
            bit_vector[i] = 1 - bit_vector[i]

def genetic_algorithm(function, n_bits, n_iterations, n_population, r_crossover, r_mutation):
    iterations_to_achieve_best = 0
    # inicjowanie początkowej populacji - zadanej ilości wektorów, każdy o zadanej wielkości bitów
    population = [randint(0, 2, n_bits).tolist() for _ in range(n_population)]
    best, best_eval = 0, function(population[0])            # przyjęcie pierwszego najlepszego rozwiązania
    for gen in range(n_iterations):
        scores = [function(c) for c in population]          # ocena dla każdego osobnika
        for i in range(n_population):                       # szukanie nowego najlepszego rozwiązania
            if scores[i] > best_eval:
                best, best_eval = population[i], scores[i]
                # if best_eval == 234:
                #     return [best, best_eval, iterations_to_achieve_best]
                print("nowe naj. rozwiązanie w %d generacji --> f(%s) = %.3f" % (gen+1, population[i], scores[i]))
                iterations_to_achieve_best = gen+1
        selected = [selection(population, scores) for _ in range(n_population)]             # reprodukcja
        children = list()
        for i in range(0, n_population, 2):
            parent1, parent2 = selected[i], selected[i+1]
            for child in crossover(parent1, parent2, r_crossover):                          # krzyżowanie
                mutation(child, r_mutation)                                                 # mutowanie
                children.append(child)
        population = children                               # nowa generacja, przejście do kolejnej iteracji
    return [best, best_eval, iterations_to_achieve_best]
