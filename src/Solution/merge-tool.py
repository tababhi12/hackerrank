def merge_the_tools(string, k):
    if 1<= len(string) <= 10000 and 1<= k <= len(string):
        listofsplit = [string[x:x+k] for x in range(0,len(string),k)]
        for y in listofsplit:
            new_element = []
            for z in range(len(y)):
                if y[z] not in new_element:
                    new_element.append(y[z])
            print(''.join(new_element))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)