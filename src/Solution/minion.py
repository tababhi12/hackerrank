def minion_game(string):
    if 0 < len(string) <= 1000000:
        total_kevin = 0
        total_stuart = 0
        kevin_vowel = 'AEIOU'
        length = len(string)
        for x in range(length):
            if string[x] in kevin_vowel:
                total_kevin = total_kevin + 1 + len(string[x+1:])
                
            else:
                total_stuart = total_stuart + 1 + len(string[x+1:])
                
        if total_kevin > total_stuart:
            print(f'Kevin {total_kevin}')
        elif total_kevin < total_stuart:
            print(f'Stuart {total_stuart}')
        else:
            print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)