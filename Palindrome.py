def pal(num):
    res = 0
    orig=num
while num !=0:
     dig = num%10
     num = num//10        #floor operator will be used not division
     res = (res*10)+dig
     print(res)
     if (orig==res):
        print("it is a palindrome")
else:
  print("it is not a palindrome ")
  x = int(input("enter a number"))
 #  pal(x)