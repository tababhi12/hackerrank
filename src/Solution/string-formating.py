def print_formatted(number):
    if 1 <= number <= 99:
        length_bin = len(bin(number)[2:])
        for x in range(1,number+1):
            dec_ = str(x)
            bin_ = bin(x)[2:]
            hex_ = hex(x)[2:].upper()
            oct_ = oct(x)[2:]
            len_dec = len(str(dec_))
            len_oct = len(oct_)
            len_hex = len(hex_)
            len_bin = len(bin_)
            dec_ = ' '*((length_bin) - len_dec) + dec_
            oct_ = ' '*((length_bin+1) - len_oct) + oct_
            hex_ = ' '*((length_bin+1) - len_hex) + hex_
            bin_ = ' '*((length_bin+1) - len_bin) + bin_
            output_string = dec_ + oct_ + hex_ + bin_
            print(output_string)
            


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)