import string

def print_rangoli(size):
    if 0 < size < 27:
        main_string = []
        alpha_list = list(string.ascii_lowercase)[:size]
        list_ = alpha_list.copy()
        alpha_list.reverse()
        alpha_list.extend(list_[1:])
        length = ((size - 1) * 2 * 2) + 1 
        for x in range(size):
            if x == 0:
                main_string.append(alpha_list.copy())
            else:
                a = len(alpha_list) // 2
                del alpha_list[a]
                del alpha_list[a]
                main_string.append(alpha_list.copy())
        joined_list = ['-'.join(x) for x in main_string]
        list__ = joined_list.copy()
        joined_list.reverse()
        for y in range(size):
            print(joined_list[y].center(length).replace(' ','-'))
        list__ = list__[1:]
        for z in range(len(list__)):
            print(list__[z].center(length).replace(' ','-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)