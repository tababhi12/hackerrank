from html.parser import HTMLParser

class myHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for ele in attrs:
            print(f'-> {ele[0]} > {ele[1]}')

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for ele in attrs:
            print(f'-> {ele[0]} > {ele[1]}')

parser = myHtmlParser()
for _ in range(int(input())):
    parser.feed(input())