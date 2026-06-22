# import time
# sec = time.time()
# min = int(time.time()/60)
# hr = int(time.time()/3600)
# print("The time now is : ", hr, min, sec)
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
# https://docs.python.org/3/library/time.html#time.strftime
if (5 <= hour < 12):
    print("Good Morning Sir")
elif (12 <= hour < 17):
    print("Good Afternoon Sir")
elif (17 <= hour < 20):
    print("Good Evening Sir")
else:
    print("Good Night Sir")
