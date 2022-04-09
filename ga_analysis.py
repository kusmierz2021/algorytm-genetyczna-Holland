from genetic_algorithm import genetic_algorithm
import matplotlib.pyplot as plt

n_iterations = 1000                             # liczba iteracji
n_bits = 18                                     # liczba cech osobnika - bitów w wektorze binarnym
n_population = 16                               # rozmiar populacji ( dla mojej implementacji wymagany jest parzysty )
r_crossover = 0.9                               # współczynnik krzyżowania typowy dla algorytmu Hollanda
r_mutation = 1.0 / float(n_bits)                # współczynnik mutowania - zależny od ilości cech pojedynczego osobnika

values_to_check = {                                         # przyporządkowanie kolejnych liczb
    "000": -4,                                              # całkowitych za pomocą kodu Graya
    "001": -3,
    "011": -2,
    "010": -1,
    "110": 0,
    "111": 1,
    "101": 2,
    "100": 4
}


def convert(x):
    check = []
    for i in range(0, len(x), 3):
        to_convert = x[i:i + 3]                             # dekodowanie kolejnych wartości z kodu Graya
        check.append(values_to_check[''.join([str(b) for b in to_convert])])
    return check


def function(x):                                            # funkcja do maksymalizowania
    check = convert(x)
    return -(sum([z ** 4 - 16 * z ** 2 + 5 * z for z in check]) / 2)


# kod poniżej użyty do wygenerowania wykresów do analizy - w celu uniknięcia błędów należy ustawić n_iterations na 25000
# oraz odkomentować w genetic_algorithm.py linię 37 i 38, które przerywaja działanie algorytmu od razu po znalezieniu
# optymalnego rozwiązania - znacząco skraca czas symulacji
# warto rowniez zakomentowac linie 39 w celu zachowania przejrzystosci informacji wyswietlanych w terminalu

# x = [i+1 for i in range(60)]
# print(x)
# n_pop_to_test = [4, 6, 8, 10, 14, 20, 36, 60, 84, 120, 160, 250, 500, 900, 1500, 3000, 7000, 18000, 30000]
#
# averages = {}
#
# for n_population in n_pop_to_test:
#     iterations = []
#     for i in range(60):
#         best, best_eval, needed_iterations = genetic_algorithm(function, n_bits, n_iterations, n_population,
#                                                                r_crossover, r_mutation)
#         if best_eval == 234:
#             iterations.append(needed_iterations)
#     print(iterations)
#
#     plt.scatter(x, iterations, s=200, color='red',
#                 alpha=0.8, marker='.', edgecolors='black')
#     plt.xlabel("numer proby")
#     plt.ylabel("liczba potrzebnych iteracji")
#     average = sum(iterations)/float(len(iterations))
#     averages[n_population] = average
#     plt.title("liczba potrzebnych iteracji dla populacji o liczebnosci wynoszacej %d\nsrednio: %.2f" %
#               (n_population, average))
#
#     plt.show()
#
#
# plt.scatter(n_pop_to_test, [averages[x] for x in n_pop_to_test],  s=200, color='blue',
#                                         alpha=0.8, marker='.', edgecolors='black')
# plt.xlabel("liczebnosc populacji")
# plt.ylabel("srednia liczba potrzebnych iteracji")
# plt.title("srednia liczba potrzebnych iteracji dla populacji o danej liczebnosci")
# plt.show()

best, best_eval, needed_iterations = genetic_algorithm(function, n_bits, n_iterations, n_population, r_crossover,
                                                       r_mutation)
print('Najlepsze uzyskane rozwiązanie --> f(%s) = %f w %d iteracji' % (convert(best), best_eval, needed_iterations))
