def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort()
    n = len(ranked)
    i = 0
    result = []

    for score in player:
        while i < n and ranked[i] <= score:
            i += 1
        result.append(n-i+1)
    return result

# problem can be found at https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
