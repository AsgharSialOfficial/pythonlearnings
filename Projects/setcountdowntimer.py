import time 
seconds = int(input('Enter your time in seconds'))
while seconds >= 0:
    min = seconds//60
    sec = seconds %60
    print(f"{min:02d}:{sec:02d}", end='\r')
    time.sleep(1)
    seconds-=1
print('Times Up')