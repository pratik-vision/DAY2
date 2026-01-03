# Q1:fibonaci seriess:
c=0
num=int(input('enter num='))
x=0
y=1
c=2
print('fibonaci series=')
print(x)
print(y)
while c<num:
    z=x+y
    print(z)
    x=y
    y=z
    c+=1

# Q2:even or odd
for n in range(1,10):
    if n % 2 ==0:
     print('even number=',n)
    else:
      print('odd number',n)

# Q3:leap year or not
n=int(input('enter year='))
if (n % 4==0 and n % 100!=0 or n % 400==0 ):
    print('leap year',n)
else:
    print('not leap year',n)

# Q4:prime or not
n=int(input('enter='))

if n<=1:
    print('not prime')
else:
    for i in range(2,int(n**0.5)+ 1):
        if  n % i==0:
            print('not prime')
            break
    else:
        print('prime')

# Q5:factorial
n=int(input('enter num='))
fact=1
if n <0:
    print('fcatorial does not exists for negative numbers')
else:

  for i in range(1,n +1):
    fact*= i
    print(fact)



# Q6:1 to 100
count=0
while count<100:
    print(count)
    count+=1

# Q7:tables
n=int(input('enter num='))
for i in range(1,11):
    o=n * i
    print(f"{n}*{i}=={o}")

# Q8:calculator
a=int(input('var1='))
b=int(input('var2='))
print("+ , - , * , / ")
op=input("enter the choice=")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op ==" *":
    print(a* b)
elif op == " /":
    print(a/b)

# Q9:pattern
for i in range (1,8):
    print("*"*i)

# Q10:GCD
a=int(input('var1='))
b=int(input('var2='))
while b !=0:
    a,b=b,a % b
    print('GCD=',a)
