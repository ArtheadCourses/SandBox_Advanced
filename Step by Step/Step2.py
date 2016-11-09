#Step two. Finding <a> tags
import urllib.request
from html.parser import HTMLParser
from urllib import parse

class Parser(HTMLParser):
    def __init__(self, url):
        super().__init__()
        self.baseUrl = url

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    print("Found link ->", newUrl)


def main():
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()

    p = Parser('http://python.org/')
    p.feed(html.decode('UTF-8'))


if __name__ == '__main__':
    main()