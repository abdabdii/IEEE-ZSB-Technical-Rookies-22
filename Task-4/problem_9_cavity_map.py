def cavityMap(grid):
    print(grid)
    finalGrid = [list(x) for x in grid]
    print(finalGrid)
    for indexRow, row in enumerate(grid):
        if indexRow != 0 and indexRow != len(grid)-1:
            for valueIndex, value in enumerate(row):
                if valueIndex != 0 and valueIndex != len(grid)-1:
                    top = grid[indexRow-1][valueIndex]
                    below = grid[indexRow+1][valueIndex]
                    left = grid[indexRow][valueIndex-1]
                    right = grid[indexRow][valueIndex+1]
                    if value > max(top, below, left, right):
                        finalGrid[indexRow][valueIndex] = 'X'
    finalGrid = [''.join(x) for x in finalGrid]
    return finalGrid


# Check problem at https://www.hackerrank.com/challenges/cavity-map/problem
