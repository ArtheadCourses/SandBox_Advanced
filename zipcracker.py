import zipfile
def main():
    zFile = zipfile.ZipFile('Secret2.zip')
    #passFile = open('dictionary.txt')
    #for line in passFile.readlines():
    #    password = line.strip('\n')
    try:
        zFile.extractall(pwd="")

        exit(0)
    except Exception as e:
        print("Fail")
    
if __name__ == '__main__':
    main()