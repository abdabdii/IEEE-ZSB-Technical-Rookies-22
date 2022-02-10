# This solution depends on mathmatics in order to solve the problem
# For the X axis we have time (t)
# For the Y axis we have the actual postition which can be calculated
# from y = x + v*t (x is the input that is given by the user and v is the velocity given by the user)
# If the two line intersects and the X,Y coordinates are integars then this prints YES otherwise NO

# This function was brought from https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not ikntersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x,y]

def getY(c,v,X):
    return c + X*v
    
def getSlope(X1,Y1,X2,Y2):
    return (Y2-Y1) / (X2-X1)
    
    
def kangaroo(c1, v1, c2, v2):
    X1 = 5
    X2 = 11
    YOfFirstEq = [getY(c1,v1,X1) , getY(c1,v1,X2)]
    YOfSecondEq = [getY(c2,v2,X1) , getY(c2,v2,X2)]
    slopeOfFirstEq = getSlope(X1,YOfFirstEq[0],X2,YOfFirstEq[1])
    slopeOfSecondEq = getSlope(X1,YOfSecondEq[0],X2,YOfSecondEq[1])
    line1 = [[X1,YOfFirstEq[0]] , [X2,YOfFirstEq[1]]]
    line2 = [[X1,YOfSecondEq[0]] , [X2,YOfSecondEq[1]]]
    if slopeOfFirstEq > slopeOfSecondEq :
        pointOfIntersection = line_intersection(line1,line2)
        checkIfIntegar = pointOfIntersection[0].is_integer() and pointOfIntersection[1].is_integer()
        if checkIfIntegar:
            return 'YES'
    return 'NO'
    


first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

result = kangaroo(x1, v1, x2, v2)
print(result)
