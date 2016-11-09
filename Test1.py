


def main():
    value = 12345
    myli = (value**value for value in range(50000))
    for i,x in enumerate(myli):
        print(i, '->', len(str(x)))
    
if __name__ == '__main__':
    main()