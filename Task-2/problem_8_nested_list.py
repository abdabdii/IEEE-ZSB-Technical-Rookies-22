def findMin(numbersList : list):
    minValue = None
    for number in numbersList:
        if minValue is None or number < minValue:
            minValue = number
    return minValue

def findSecondLowest(numbersList : list):
    secondMin = findMin(numbersList)
    removedMin = list(filter(lambda a: a != secondMin, numbersList))
    return findMin(removedMin)

def filterStudentsByScore(student : list , secondLowestScore : float):
    if student[1] == secondLowestScore:
        return True
    else:
        return False

def getStudentsNames(student : list):
    return student[0]
        
def findStudentsWithSecondLowest(students : list):
    scores = []
    for student in students:
        scores.append(student[1])
    secondLowest = findSecondLowest(scores)
    studentsList = filter(lambda student: filterStudentsByScore(student, secondLowest),students)
    studentsNames = map(getStudentsNames, list(studentsList))
    studentsNames = list(studentsNames)
    return sorted(studentsNames)

students = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
studentNames = findStudentsWithSecondLowest(students)
print('\n'.join(studentNames))