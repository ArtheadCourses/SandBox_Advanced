import time, sched

def print_msg(msg="Default Message"):
    print("Scheduled message:", msg)


def main():
    s = sched.scheduler()
    s.enter(10,1,print_msg)
    s.enter(3,2,print_msg, ('New Message',))
    s.enter(3,1,print_msg, ('Newer Message',))
    s.run()
    #time.sleep(30)
    
if __name__ == '__main__':
    main()