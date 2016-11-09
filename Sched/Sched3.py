import sched
#A way to get rid of globals is to create a wrapper that can hold
#references to unchangable objects, such as s and n
def wrapper(s, n= 10):
    def sched_func(counter=0):
        counter += 1
        print("Whaaat! This is the", counter, "time I'm here")
        if counter < n:
            s.enter(3,1,sched_func, (counter, ))

    # Return reference to inner function so it can be scheduled
    return sched_func

def main():
    #Before Python 3.3 we had to do this
    #s = sched.scheduler(time.time, time.sleep)
    s = sched.scheduler()
    s.enter(3,1,wrapper(s, 3))
    s.run()
    
if __name__ == '__main__':
    main()