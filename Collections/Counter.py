import collections
from re import split
def main():
    text = "John, Sue and Paul likes music. Paul likes whatever Sue likes but Sue does not like John's music. What John likes, nobody knows."
    #Using regex split to split at anything but letters and ', skipping the last
    #item as it will be an empty string
    words = split(r"[^a-z\']+", text.lower())[:-1]
    print(words)
    c = collections.Counter(words)
    print(c)
    print(c.most_common())
    for word in c.most_common(3):
        print(word[0], '->', word[-1])
    
if __name__ == '__main__':
    main()