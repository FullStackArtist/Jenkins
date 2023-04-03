for _ in range(int(input())):
    S1=input("")
    S2=input("")
    flag=0
    k=0
    while True:
        if flag==0:
            for (i,j) in zip(S1,S2):
                k=k+1
                if i is j:
                    pass
                else:
                    if j is '*' or i is '*':
                        if k==0:
                            flag=2
                            break
                        else:
                            k==0
                            flag=1
                            break

        else:
            break
    if flag==1:
        print("True")
    else:
        print("False")
                    
