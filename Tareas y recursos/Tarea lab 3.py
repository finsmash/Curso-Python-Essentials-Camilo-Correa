# lab 3 listas y return 3

def isYearLeap(year):
    if year>1582:
        if (year%4)==0 and (year%100)==0 and (year%400)==0:
            return True
        else:
            return False
    else:
        return None
 
def daysInMonth(year, month):
    diasPorMes = [31,28,31,30,31,30,31,31,30,31,30,31]
 
    if isYearLeap(year):
        if diasPorMes[month - 1] == 28:
            return (29)
        else:
            return(diasPorMes[month - 1])
    else:
        return(diasPorMes[month - 1])
 
    return (None)
 
def dayOfYear(year, month, day):
 
    if year < 1582 or month > 12 or month < 1:
        return (None)
 
    if day > daysInMonth(year, month) or day < 1:
        return(None)
 
    totalDias = day
    month = month -1
    while month > 0:
        totalDias += daysInMonth(year, month)
        month -= 1
    return (totalDias)
 
 
print(dayOfYear(2000, 12, 31))

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
              yr = testYears[i]
              mo = testMonths[i]
              print(yr, mo, "->", end="")
              result = daysInMonth(yr, mo)
              if result == testResults[i]:
                            print("OK")
              else:
                            print("Failed")

