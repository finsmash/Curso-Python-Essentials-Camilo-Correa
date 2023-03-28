# lab 1 listas y return 1

def isYearLeap(year):
    if year>1582:
        if (year%4)==0 and (year%100)==0 and (year%400)==0:
            return True
        else:
            return False
    else:
        return None

testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):
            yr = testData[i]
            print(yr,"->",end="")
            result = isYearLeap(yr)
            if result == testResults[i]:
                        print("OK")
            else:
                        print("Failed")