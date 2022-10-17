#cheating variant
def swap_case(s):
    return s.swapcase()

#better variant with dictionary/ two list, same indexes, going through it with for loop

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)