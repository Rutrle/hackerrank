if __name__ == '__main__':
    x = 1
    y = 1
    z = 1
    n = 2
    my_list = [[k,l,m] for k in range(x+1) for l in range(y+1) for m in range(z+1) if k+l+m!=n]

    print(my_list)