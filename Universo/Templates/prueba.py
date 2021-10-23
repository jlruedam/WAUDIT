print(6%2)

def fizzBuzz(n):
    # Write your code here
    if 0<n<2e5:
        
        n+=1
        for i in range(1,n):
            if i%3==0 and i%5==0:
                print("FizzBuzz")
            elif i%3==0 and i%5!=0:
                print("Fizz") 
            elif i%3!=0 and i%5==0:
                print("Buzz") 
            else:
                print(i)
                

fizzBuzz(15)