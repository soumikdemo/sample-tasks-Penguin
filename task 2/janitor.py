
weight = [1.01, 1.99, 2.5, 1.5, 1.01] 
#weight = [1.01, 1.01, 1.01, 1.4, 2.4]
#weight = [1.01, 1.991, 1.32, 1.4]


def efficientJanitor(weight):                                        #function declaration
    weight.sort(reverse = True)                                      #sorted high to low
    tripList = []                                                    #list of items per trip

    if len(weight)<1 or len(weight)>1000:
        return "zero or number of plastic bags more than 1000!" 

    for item in weight:
        if not(1.01 <= item <= 3.0):
            return "weight criteria not fulfilled"            

    while len(weight)>0:
        temp = []
        temp.append(weight[0])
        weight.pop(0) 

        for item in weight:
            if sum(temp)+item <= 3.00:
                temp.append(item)
                weight.remove(item)

        tripList.append(temp)

    print("\nThe janitor can carry all plastic bags out in "+ str(len(tripList)) +" trips: ")
    print(tripList)

    return len(tripList)


result = efficientJanitor(weight)
print(result)


