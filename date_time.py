import datetime

def get_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    return time

def get_date():
    year=str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    date = year + "-" + month + "-" + day
    return date

def wishing():
    h = datetime.datetime.now().hour
    
    if h>0 and h<12:
        wish = "Good Morning"
    elif h>=12 and h<15:
        wish = "Good Afternoon"
    elif h>=15 and h<19:
        wish = "Good Evening"
    else:
        wish = "Good Night"

    return wish


print("The Time is : ", get_time())
print("The Date is : ", get_date())
print(wishing())
