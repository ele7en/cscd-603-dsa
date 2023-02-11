INT_MAX = 2147483647


def optimal_search_tree(keys: list, freq: list, n: int) -> int:
    cost = [[0 for x in range(n + 1)] for y in range(n + 1)]

    for i in range(n):
        cost[i][i] = freq[i]

    print("===>>>>", cost)

    # Now we need to consider chains of length 2, 3, ... L is chain length.
    for L in range(2, n + 1):

        # i is row number in cost
        for i in range(n - L + 1):

            # Get column number j from row number i and chain length L
            j = i + L - 1
            off_set_sum = sum(freq, i, j)

            if i >= n or j >= n:
                break
            cost[i][j] = INT_MAX

            # Try making all keys in interval keys[i..j] as root
            for r in range(i, j + 1):

                # c = cost when keys[r] becomes root of this subtree
                c = 0
                if r > i:
                    c += cost[i][r - 1]
                if r < j:
                    c += cost[r + 1][j]
                c += off_set_sum
                if c < cost[i][j]:
                    cost[i][j] = c

    return cost[0][n - 1]


# A utility function to get sum of array elements freq[i] to freq[j]
def sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


# Driver Code
if __name__ == "__main__":
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    n = len(keys)
    print(n)
    print("Cost of Optimal BST is", optimal_search_tree(keys, freq, n))
