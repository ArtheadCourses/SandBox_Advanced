#Step one. Getting a single web page
import urllib.request
def main():

    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()

    print(html.decode('UTF-8'))

if __name__ == '__main__':
    main()