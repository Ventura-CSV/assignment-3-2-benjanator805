def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    
    ########################################
    if num1 <= num2 and num1 <= num3:
        minval = num1
    elif num2 <= num3 and num2 <= num1:
        minval = num2
    elif num3 <= num1 and num3 <= num2:
        minval = num3
    
    if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
        median = num1
    elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
        median = num2
    elif (num3 >= num2 and num3 <= num1) or (num3 <= num2 and num3 >= num1):
        median = num3
    
    if num1 >= num2 and num1 >= num3:
        maxval = num1
    elif num2 >= num1 and num2 >= num3:
        maxval = num2
    elif num3 >= num1 and num3 >= num2:
        maxval = num3
    ########################################
    

    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
