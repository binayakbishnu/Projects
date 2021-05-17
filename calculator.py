c=1
while c >0:
    num1=int(input('Enter first number: '))
    num2=int(input('Enter second number: '))
    op=input('Enter operator: ')
    if(op=='+'):
        print('\nSum of ',num1,' and ',num2,'is: ',num1+num2)
    elif(op=='-'):
        print('\nDifference of ',num1,' and ',num2,'is: ',num1-num2)
    elif(op=='*'):
        print('\nProduct of ',num1,' and ',num2,'is: ',num1*num2)
    else:
        quo=float(num1/num2)
        print('\nDivision of ',num1,' by ',num2,'gives: ',quo)
    c=int(input('Continue? 0/1: '))

print("Thank you")