nterms = int (input("How many terms to be printed: "))

n1 = 0
n2 = 1
count = 0

if nterms <=0:
    print("P;ease enter a positive integer,the given number is not valid")

elif nterms ==1 :
    print("The Fibonacci sequence of the numbers up to",nterms,":")
    print(n1)

else:
    print("The fibonacci sequence of the number is :")
    while count < nterms:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1
