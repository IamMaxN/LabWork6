def calculate_weights(matrix):
    n = len(matrix)
    row_sums = [sum(row) for row in matrix]
    normalized_matrix = [[element / row_sum for element in row] for row, row_sum in zip(matrix, row_sums)]
    column_sums = [sum(col) for col in zip(*normalized_matrix)]
    weights = [col_sum / n for col_sum in column_sums]
    return weights

def main():
    n = int(input("Введите количество критериев: "))
    criteria_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        criteria_matrix[i][i] = 1

    for i in range(n):
        for j in range(i + 1, n):
            pairwise_comparison = float(input(f"Введите отношение важности критерия {i + 1} к критерию {j + 1} (от 1 до 9): "))
            criteria_matrix[i][j] = pairwise_comparison
            criteria_matrix[j][i] = 1 / pairwise_comparison

    weights = calculate_weights(criteria_matrix)

    print("Весовые коэффициенты:")
    for i, weight in enumerate(weights):
        print(f"Критерий {i + 1}: {weight:.2f}")

if __name__ == "__main__":
    main()
