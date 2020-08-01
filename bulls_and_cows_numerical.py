def check(num):
    for i in num:
        pos=num.index(i)
        for j in range(pos+1,len(num),1):
            if i == num[j]:
                return 0
    return 1


print("Welcome to Bulls and Cow numerical version")
print("Enter the secret number!!\n\tMAKE SURE THE OPPONENT DOES NOT SEE YOUR NUMBER!")
se_num=input()
secret=[]
for i in se_num:
    secret.append(i)
while True:
    if check(secret)==1:
        break
    else:
        print("Enter a valid secret number !")
        se_num=input()
        secret=[]
        for i in se_num:
            secret.append(i)
print ("Entered to the game!")
print ("Start guessing the number, opponent !")
tries=0
while True:
    tries=tries+1
    print("Enter your "+str(tries)+" try")
    num=input()
    num_list=[]
    for i in num:
        num_list.append(i)
    bulls,cows=0,0
    for i in num_list:
        pos=num_list.index(i)
        if i==secret[pos]:
            bulls=bulls+1   
        else:
            if i in secret:
                cows=cows+1
    if bulls==len(secret):
            no_of_try=tries
            print("You found the secret number")
            print("You took "+str(no_of_try)+" tries")
            break
    print("Number of bulls: "+str(bulls))
    print("Number of cows: "+str(cows))
print("End of the game !!!!")
