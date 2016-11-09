#Step three. Build a better class
import urllib.request
from html.parser import HTMLParser
from urllib import parse
import threading

class Parser(HTMLParser):
    def __init__(self, url):
        super().__init__()
        self.baseUrl = url
        self.visted = []


    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    if newUrl not in self.visted:
                        self.pages_to_visit.append(newUrl)

    def spider_page(self, word):
        if not self.pages_to_visit:
            return
        url = self.pages_to_visit.pop()
        if self.baseUrl not in url:
            return 0
        self.visted.append(url)
        #print("Spider page", url)
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read()
            #    if response.getheader('Content-Type') == 'text/html':

                self.feed(html.decode('utf-8'))
                if word in html.decode('utf-8'):
                    print("Found at", url)
                    self.word_found_at.append(url)
        except:
            #print("Error reading", url)
            pass
        return 1

    def start_spider(self, word, max_pages):
        self.pages_to_visit = [self.baseUrl]
        self.word_found_at = []
        pages_visited = 0
        while pages_visited < max_pages and self.pages_to_visit:
            pages_visited += self.spider_page(word)


def main():
    p = Parser('http://nytimes.com/')
    word = "Trump"
    thread_list =[]
    for _ in range(10):
        t = threading.Thread(target=p.start_spider,args=(word,300))
        t.start()
        thread_list.append(t)
        # p.start_spider(word, 10)
    for t in thread_list:
        t.join()

    for link in p.word_found_at:
        print(word,'found at', link)

if __name__ == '__main__':
    main()