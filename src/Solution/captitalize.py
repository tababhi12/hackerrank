def solve(s):
    if 0 < len(s) < 1000:
        main_string = s
        s = s.replace(' ','')
        if s.isalnum():
            main_list = [x.capitalize() for x in main_string.split(' ')]
            print(' '.join(main_list))

            
if __name__ == '__main__':
    s = input()
    result = solve(s)    