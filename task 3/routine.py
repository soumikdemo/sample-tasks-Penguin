
import collections 
import numpy as np
from collections import defaultdict


courseByTeacher = collections.OrderedDict()
courseByTeacher['English Grammar'] = 'John Smith' 
courseByTeacher['Mathematics'] = 'Lara Gilbert'
courseByTeacher['Physics'] = 'Johanna Kabir'
courseByTeacher['Chemistry'] = 'Danniel Robertson'
courseByTeacher['Biology'] = 'Larry Cooper'

dayArr = [["not created","not created","not created","not created"] for _ in range(5)]



def createRoutine(day, hClass, courseIndex):
    courses = list(courseByTeacher.keys())
    dayArr[day][hClass]=courses[courseIndex] 
    


def optionC():
    for _, (key, value) in enumerate(courseByTeacher.items()):      
        print(key+",", value) 
    
    userInput = input()
    if userInput == 'M':
        main()
    elif userInput == 'B':
        optionB()
    elif userInput == 'A':
        optionA()
    else:
        print("Wrong input")


def optionB():
    for x in dayArr:
        for y in x:
            print(dayArr.index(x), x.index(y), y)
            #print(y) 

        print("\n")


def optionA():
    for i, (key, _) in enumerate(courseByTeacher.items()):      
        print(str(i)+".", key) 

    print("\nTo create a routine follow the pattern: \ndayIndex(0 - 4) hourIndex(0 - 3) courseIndex\n") 
    print("Type routine pattern. Press Ctrl-Z in new line & enter to create it.")
    
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)

    #print(contents)
    for x in contents:
        indexes = x.split() 
        day = int(indexes[0])
        hClass = int(indexes[1])
        course = int(indexes[2])

        print(day, hClass, course)
        createRoutine(day, hClass, course)
    
    main()



def main():
    print("\nChoose from the following options: (A,B,C and M to see options again)")
    print("A. Create Routine \nB. Show Routine \nC. List Courses with Teachers Name")

    userInput = input('\nType & Enter ---------->')

    if userInput == 'C':
        optionC()
    elif userInput == 'B':
        optionB()
    elif userInput == 'A':
        optionA()
    else:
        print("Wrong input")




class Routine:
   'Common base class for school'
   userCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Routine.userCount += 1 


#Objects created here -----------------------
#emp1 = Employee("Zara", 2000) 
#emp2 = Employee("Manni", 5000)



main()



    


#for i, (key, value) in enumerate(courseByTeacher.items()):
    #print(i, key, value)
#print(courseByTeacher.keys())

# test = {}
# innerDict = {}

# for x in range(4):
#     innerDict[x]="not created"

# for y in range(5):
#     test[y]=innerDict


#print(test)
#arr = np.array(["not created","not created","not created","not created"])
#arr = ["not created","not created","not created","not created"]
#dayArr = np.array([])
#for x in range(5):
    #dayArr = np.append(dayArr, arr)