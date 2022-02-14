def acmTeam(topic):
    longestCouple = 0
    counter = 0
    for i in range(len(topic)):
        for j in range(i, len(topic)):
            sub = 0
            for x, y in zip(topic[i], topic[j]):
                if x == '1' or y == '1':
                    sub += 1
            if sub > longestCouple:
                longestCouple = sub
                counter = 1
            elif sub == longestCouple:
                counter += 1

    return [longestCouple, counter]

# problem can be found at https://www.hackerrank.com/challenges/acm-icpc-team/problem
