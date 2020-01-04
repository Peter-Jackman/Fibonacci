def fib(x):
    ans=0
    if x==1:
        ans=1
    elif x==2:
        ans=1
    else:
        first=1
        number=1
        nist=1
        for n in range(x-2):
            nist=first
            first=first+number
            number=nist
            ans=first
    return ans

def player_input(correct_input, incorrect_input, question):

    while True:
        output=input(question)
        if output==correct_input:
            x=1
            break

        elif output==incorrect_input:
            x=0
            break
        
        else:
            print(f'Please input {correct_input}/{incorrect_input}')
    return x

x=1
while x==1:
    num=int(input('How many do you want?'))     
    print(fib(num))
    x=player_input('yes','no','Do you want to try again? yes/no?')
