# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class myHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'{tag}')
        for ele in attrs:
            print(f'-> {ele[0]} > {ele[1]}')

    def handle_startendtag(self, tag, attrs):
        print(f'{tag}')
        for ele in attrs:
            print(f'-> {ele[0]} > {ele[1]}')


parser = myHtmlParser()
for _ in range(int(input())):
    parser.feed(input())