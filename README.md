## Optimal Binary Search Tree
An optimal binary search implementation with python.


The cost of the optimal binary search tree (OBST) depends on the keys and their frequencies of occurrence. The cost is defined as the expected number of comparisons needed to search for an item in the tree.

To find the cost of the OBST for the given keys and frequencies, we first construct a table to store the cost of each subtree. The cost of a subtree rooted at node i is the sum of frequencies of all the keys in the subtree plus the cost of the optimal binary search tree of the subtree. The final cost of the OBST is the value in the cell corresponding to the root of the tree (i.e., the value in the cell (1, n), where n is the number of keys).

Here's the algorithm to calculate the cost of the OBST:

- Initialize a 2D table "cost" of size nxn, where n is the number of keys.
- Fill the diagonal of the table with the frequencies.
- For each subproblem of size len (length) from 2 to n, do the following:
  - For each node i from 1 to n-len+1, do the following:
      - Calculate node j as i+len-1.
      - Calculate the cost of the subtree rooted at node i, with keys ranging from i to j.
      - Find the minimum cost of all subtrees rooted at nodes k (i <= k <= j) by using the formula:

    cost[i][j] = min(cost[i][j], cost[i][k-1] + cost[k+1][j] + sum[j] - sum[i-1]), where sum is an array storing the prefix sum of frequencies.
- The cost of the OBST is stored in cost[1][n].

```bash
0  [0, 34, 42,  92]
10 [0,  0, 50, 100]
12 [0,  0,  0,  58]
20 [0,  0,  0,   0]

And the cost of the OBST is cost[1][3] = 58.
```

In this case, n=3, so the table cost will have the following form: