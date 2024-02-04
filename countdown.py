from time import sleep


def countdown(i):
    sleep(1)
    print (i)
    if i <= 1:
        return
    else:
        countdown(i-1)
countdown(100)