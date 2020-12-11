import itertools

file = open('input.txt', 'r')
input = [int(x.strip()) for x in file.readlines()]

input.append(max(input) + 3)
input.append(0)

input.sort()

DP = {}
def dp(i):
    if i == len(input)-1:
        return 1
    if i in DP != None:
        return DP[i]
    ans = 0
    for j in range(i+1, len(input)):
        if input[j] - input[i] <= 3:
            ans += dp(j)
    DP[i] = ans
    return ans

print(dp(0))