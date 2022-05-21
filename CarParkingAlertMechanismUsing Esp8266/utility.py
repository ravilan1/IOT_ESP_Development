from utime import localtime

class Utility:
    #staticMethod
    def getCurrentLocalTime():
        dateTimeObj = localtime()
        Dyear, Dmonth, Dday, Dhour, Dmin, Dsec, Dweekday, Dyearday = (dateTimeObj)
        Ddateandtime = "{}-{}-{} {}:{}"
        print(Ddateandtime.format(Dday, Dmonth, Dyear, Dhour, Dmin,))
        return Ddateandtime.format(Dday, Dmonth, Dyear, Dhour, Dmin,)
    
    #getCurrentLocalTime()
