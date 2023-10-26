def calculate_weights(n):
    criteria = []
    pairwise_comparisons = []
    
    # Ввод данных
    for i in range(n):
        criterion = input(f"Введите название критерия {i+1}: ")
        criteria.append(criterion)
        
    for i in range(n):
        for j in range(i+1, n):
            comparison = float(input(f"Введите попарное сравнение для критериев {criteria[i]} и {criteria[j]} (отношение важности): "))
            pairwise_comparisons.append(comparison)
            
    # Расчет весовых коэффициентов
    matrix = []
    k = 0
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            elif i < j:
                row.append(pairwise_comparisons[k])
                k += 1
            else:
                row.append(1 / pairwise_comparisons[k-1])

                k -= 1
        matrix.append(row)
    
    weights = []
    for i in range(n):
        weight = 1
        for j in range(n):
            weight *= matrix[i][j]
        weight = weight ** (1/n)
        weights.append(weight)
        
    # Вывод результатов
    print("Весовые коэффициенты:")
    for i in range(n):
        print(f"{criteria[i]}: {weights[i]:.2f}")

# Пример использования
n = int(input("Введите количество критериев: "))
calculate_weights(n)
