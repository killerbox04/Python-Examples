#Testing
import random
import time
testString = 0
subStringA = 0
subStringB = 0
subStringC = 0

while True:
    print(testString)
    print(subStringA + subStringB + subStringC)
    inputA = random.randint(0,9999)
    inputB = random.randint(0,9999)
    inputC = random.randint(0,9999)

    testString = f"{inputA}:{inputB}:{inputC}"
    strL = len(testString)


    #Index method "start" parameter is inclusive and starts at 0
    C1P = testString.index(":")               #Colon 1 position
    C2P = testString.index(":",C1P + 1, strL) #Colon 2 position



    subStringA = testString[:C1P]
    subStringB = testString[C1P+1:C2P]
    subStringC = testString[C2P+1:]

    time.sleep(1)    

