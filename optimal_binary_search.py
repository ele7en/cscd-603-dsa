def optimal_bst(keys, freq):
    n = len(keys)

    cost = [[0 for j in range(n + 1)] for i in range(n + 1)]

    sum = [0 for i in range(n + 1)]

    for i in range(1, n + 1):
        sum[i] = sum[i - 1] + freq[i - 1]

    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1
            cost[i][j] = float("inf")

            for k in range(i, j + 1):
                c = cost[i][k - 1] + cost[k][j] + sum[j] - sum[i - 1]
                if c < cost[i][j]:
                    cost[i][j] = c

    # return cost[1][n]
    return cost


keys = [10, 20, 30, 40]
freq = [4, 2, 6, 3]
print("Cost of the optimal binary search tree is:", optimal_bst(keys, freq))
