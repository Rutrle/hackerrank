if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    high=-100
    second=-100
    for num in arr:

        if num > high:
            second=high
            high=num
        elif num>second and num !=high:       
            second=num
            
      
    print(second)
