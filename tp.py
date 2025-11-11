import random
import time
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Metrics:
    n: int
    comparisons: int
    moves: int
    time: float


# ========== Merge Sort ==========
def merge_sort(arr):
    comparisons = 0
    moves = 0

    def merge(left, right):
        nonlocal comparisons, moves
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                moves += 1
                i += 1
            else:
                result.append(right[j])
                moves += 1
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        moves += len(left[i:]) + len(right[j:])
        return result

    def recursive_merge_sort(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        left = recursive_merge_sort(sub_arr[:mid])
        right = recursive_merge_sort(sub_arr[mid:])
        return merge(left, right)

    start_time = time.time()
    sorted_arr = recursive_merge_sort(arr)
    elapsed = time.time() - start_time
    arr[:] = sorted_arr
    return Metrics(len(arr), comparisons, moves, elapsed)


# ========== Quick Sort (pivot aléatoire) ==========
def quick_sort(arr):
    comparisons = 0
    moves = 0

    def partition(low, high):
        nonlocal comparisons, moves
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        moves += 1
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                moves += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        moves += 1
        return i + 1

    def recursive_quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            recursive_quick_sort(low, pi - 1)
            recursive_quick_sort(pi + 1, high)

    start_time = time.time()
    recursive_quick_sort(0, len(arr) - 1)
    elapsed = time.time() - start_time
    return Metrics(len(arr), comparisons, moves, elapsed)


# ========== Tests ==========
def test_algorithms():
    sizes = [1000, 5000, 10000, 50000, 100000, 1000000, 10000000]
    types = ['random', 'sorted', 'reversed']
    results = []

    for n in sizes:
        for t in types:
            if t == 'random':
                arr = [random.randint(0, n) for _ in range(n)]
            elif t == 'sorted':
                arr = list(range(n))
            else:
                arr = list(range(n, 0, -1))

            # Merge Sort
            arr_copy = arr.copy()
            merge_metrics = merge_sort(arr_copy)

            # Quick Sort
            arr_copy = arr.copy()
            quick_metrics = quick_sort(arr_copy)

            results.append((n, t, 'MergeSort', merge_metrics))
            results.append((n, t, 'QuickSort', quick_metrics))

    return results


# ========== Exécution ==========
results = test_algorithms()

# Affichage tableau
print(f"{'Taille':<10}{'Type':<10}{'Algorithme':<12}{'Comparaisons':<15}{'Déplacements':<15}{'Temps (s)':<10}")
for n, t, alg, m in results:
    print(f"{n:<10}{t:<10}{alg:<12}{m.comparisons:<15}{m.moves:<15}{m.time:<10.5f}")

# ========== Graphique comparatif ==========
plt.figure(figsize=(10,6))
colors = {'random': 'blue', 'sorted': 'green', 'reversed': 'red'}

for t in ['random', 'sorted', 'reversed']:
    merge_times = [m.time for n, tt, alg, m in results if alg == 'MergeSort' and tt == t]
    quick_times = [m.time for n, tt, alg, m in results if alg == 'QuickSort' and tt == t]
    sizes = [n for n, tt, alg, m in results if alg == 'MergeSort' and tt == t]

    plt.plot(sizes, merge_times, marker='o', color=colors[t], linestyle='-', label=f"MergeSort ({t})")
    plt.plot(sizes, quick_times, marker='s', color=colors[t], linestyle='--', label=f"QuickSort ({t})")

plt.title("Comparaison du temps d’exécution: MergeSort vs QuickSort")
plt.xlabel("Taille du tableau (n)")
plt.ylabel("Temps (secondes)")
plt.legend()
plt.grid(True)
plt.show()

# ========== Remarque ==========
print("\n Remarque:")
print(" QuickSort utilise un axe aléatoire pour éviter le pire des cas.")
print(" MergeSort maintient des performances constantes en O(n log n).")
print(" QuickSort est généralement plus rapide sur les tables aléatoires, mais plus lent sur les tables triées ou inversées.")