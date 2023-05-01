from random import randint

def max_up(n):
    max_lens = [1] + [0] * (len(n) - 1)
    for i in range(1, len(n)):
        if n[i] > n[i - 1]:
            max_lens[i] = max_lens[i - 1] + 1   
        else:
            max_lens[i] = 1
    return max(max_lens)

    
if __name__ == '__main__':
    # N = [4, -9, 100, 40, 89, -89, 45, 10, -45, -44, -43, -42]
    N = [randint(-100, 100) for _ in range(25)]
    print(N)

    print(max_up(N))
