def heist(exhibits, rounds, max_weight):
    stolen = []
    stolenamount = 0

    exhibits = sorted(exhibits, key=lambda x: (x[1], x[0]))

    exhibits_amount = len(exhibits)
    t = [[-1 for _ in range(max_weight + 1)] for _ in range(exhibits_amount + 1)]
    for h in range(rounds):
        for i in range(exhibits_amount): # i - стоимость
            for j in range(max_weight+1): #j - вес
                if i == 0 or j == 0:
                    t[i][j] = 0
                elif exhibits[i][1] <= j:
                    t[i][j] = max(exhibits[i][0] + t[i-1][j - exhibits[i][1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]

        while i > 0 and j > 0:
            if t[i][j] == t[i-1][j]:
                i -= 1
            else:
                exhibits_copy = exhibits[i].copy()
                stolen.append(exhibits_copy)
                stolenamount += exhibits_copy[0]
                j -= exhibits[i][1]
                exhibits[i][1] = float('inf')
                i -= 1
        return(f'{stolen} was stolen, for {stolenamount}')



if __name__ == '__main__':
    exhibits = [[100000, 9], [10000, 2], [50000, 5], [50001, 5]]

    print(f'\n # input {exhibits} \n')
    print(heist(exhibits, 1, 10), '\n')