import sys
sys.path.append('../')
from helpers import test

def rectArea(width : float , height : float):
    try:
        width = float(width)
        height = float(height)
        return {'area': round(width*height ,2), 'perimeter': round(2*width + 2*height , 2)}
    except:
        return 'Please enter a valid number'


## Tests Section Start
test1 = rectArea(5,6)
test2 = rectArea(0,0)
test3 = rectArea(5.65,6)
test4 = rectArea('str','str')

test(test1['area'] == 30 and test1['perimeter'] == 22 , 'Testing 5x6 rect')
test(test2['area'] == 0 and test2['perimeter'] == 0 , 'Testing 0x0 rect')
test(test3['area'] == 33.9 and test3['perimeter'] == 23.3 , 'Testing float value 5.65x6 rect')
test(test4 == 'Please enter a valid number' , 'Testing invalid input e.g string')
## Tests Section End


width = input('Please enter the width of the rect: ')
height = input('Please enter the height of the rect: ')

result = rectArea(width,height)
print(str(result['area']) + '\n' + str(result['perimeter']) if result != 'Please enter a valid number' else result )