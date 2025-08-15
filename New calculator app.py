class Calculator:
    k=1
    while k!='0':
        def add(a,b):
            print(f'sum is:{a+b}')

        def sub(a,b):
            print(f'difference is:{a-b}')

        def mul(a,b):
            print(f'product is:{a*b}')

        def div(a,b):
            print(f'division is:{a/b}')

        a=float(input('Enter the first number:'))
        b=float(input('Enter the second number:'))
        c=input('Enter the calculation symbol:')

        if c=='+':
            add(a,b)

        elif c=='-':
            sub(a,b)

        elif c=='*':
            mul(a,b)

        elif c=='/':
            div(a,b)

        print('')
        k=input('Enter 0 to exit (or) Press any key to exit... :')
        print('')
