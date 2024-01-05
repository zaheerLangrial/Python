import datetime


# print(datetime.datetime.now())

x = datetime.datetime.now()
print(x.year)
print(x.hour)
print(x.minute)
print(x.strftime('%A'))


        # Creating Date Objects


x = datetime.datetime(2000 , 7 , 3) 
print(x)
print(x.strftime('%B')  , x.strftime('%A'))
