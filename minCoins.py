def minCoinTopDown(lstr, n):
    set1 = {n}
    set2 = set()
    count = 1
    while True:
        for i in set1:
            for j in lstr:
                new_val = i - j
                if new_val == 0:
                    return count
                elif new_val < 0:
                    continue
                set2.add(new_val)
        count = count + 1
        if set2:
            set1 = set2
            set2 = set()
        else:
            return False

def minCoinBottomUp(lstr, n):
    result = [0] + [n + 1] * n
    for i in range(n + 1):
        for j in lstr:
            if j <= i:
                result[i] = min(result[i-j] + 1, result[i])
    return result[-1] if result[-1] < n + 1 else False

assert(minCoinTopDown([1, 2, 5], 11)) == 3
assert(minCoinTopDown([2,5,10], 1)) == False
assert(minCoinTopDown([1,5,10], 11)) == 2


assert(minCoinBottomUp([1, 2, 5], 11)) == 3
assert(minCoinBottomUp([2,5,10], 1)) == False
assert(minCoinBottomUp([1,5,10], 11)) == 2

