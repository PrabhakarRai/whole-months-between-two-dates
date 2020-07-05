from datetime import date

def isleapyear(year):
    '''/
    Returns True if given int is a leap year.
    '''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def dateInput(text, frmt=' (DD/MM/YYYY) : '):
    '''/
    Converts string input of date in format into a date object
    '''
    text += frmt
    dateIn = input(text)
    idate, imonth, iyear = map(int, dateIn.split('/'))
    return date(iyear, imonth, idate)

def wholeMonths(startdate, enddate):
    '''/
    Prints name and year of complete months between two dates (inclusive)
    '''
    daysInMonthStart = [31,28,31,30,31,30,31,31,30,31,30,31]
    daysInMonthEnd = [31,28,31,30,31,30,31,31,30,31,30,31]
    monthCounter = 0

    if isleapyear(startdate.year):
        daysInMonthStart[1] = 29
    if isleapyear(enddate.year):
        daysInMonthEnd[1] = 29
    
    fdayOfstart = date(startdate.year, startdate.month, 1)
    ldayOfend = date(enddate.year, enddate.month, daysInMonthEnd[(enddate.month-1)])

    totaldays = ((enddate - startdate).days) + 1

    fdaydif = (fdayOfstart - startdate).days
    fullMonthStart = None
    if fdaydif < 0 and startdate.month == 12:
        fullMonthStart = date((startdate.year+1), 1, 1)
    elif fdaydif < 0:
        fullMonthStart = date(startdate.year, (startdate.month+1), 1)
    else:
        fullMonthStart = date(startdate.year, startdate.month, startdate.day)
    
    edaydif = (ldayOfend - enddate).days
    fullMonthEnd = None
    if edaydif > 0 and enddate.month == 1:
        fullMonthEnd = date((enddate.year-1), 12, 31)
    elif edaydif > 0:
        fullMonthEnd = date(enddate.year, enddate.month-1, daysInMonthEnd[enddate.month-2])
    else:
        fullMonthEnd = date(enddate.year, enddate.month, enddate.day)
    
    while True:
        if (fullMonthEnd - fullMonthStart).days < 0:
            return monthCounter
        print(fullMonthStart.strftime("%B"), fullMonthStart.year)
        monthCounter += 1
        if fullMonthStart.month != 12:
            fullMonthStart = date(fullMonthStart.year, (fullMonthStart.month)+1, 1)
        else:
            fullMonthStart = date((fullMonthStart.year)+1, 1, 1)

dStart = dateInput('Enter Starting date')
dEnd = dateInput('Enter Ending date')

print('There are', wholeMonths(leaveStart, leaveEnd), 'full months between above two dates.')
