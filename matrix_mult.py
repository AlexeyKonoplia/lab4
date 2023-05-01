def matrix_multiplication(A):
    N = len(A)
    shape = [len(A[i]) for i in range(N)]
    shape.append(len(A[N - 1][0]))
    print(shape)
    dp = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0

    for length in range(2, N+1):
        for i in range(N-length+1):
            j = i + length - 1
            for k in range(i, j):
                operations = dp[i][k] + dp[k+1][j] + shape[i] * shape[k+1] * shape[j+1]
                dp[i][j] = min(dp[i][j], operations)
    print(dp)
    return dp[0][N-1]

if __name__ == '__main__':
    A = [[1] * 100 for _ in range(10)]
    B = [[1] * 5 for _ in range(100)]
    print([A, B])
    print(matrix_multiplication([A, B]), 'операций')