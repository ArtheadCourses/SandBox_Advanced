import sched
counter = 0
def sched_func(s):
    global counter
    counter += 1
    print("Whaaat! This is the", counter, "time I'm here")
    if counter < 10:
        s.enter(3,1,sched_func, (s,))


def main():
    #Before Python 3.3 we had to do this
    #s = sched.scheduler(time.time, time.sleep)
    s = sched.scheduler()
    s.enter(3,1,sched_func,(s,))
    s.run()
    
if __name__ == '__main__':
    main()