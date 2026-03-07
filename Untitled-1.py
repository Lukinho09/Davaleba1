print ("Atobitidan Orobitshi -> 1")
print ("Orobitidan Atobitshi -> 2")
print ("Atobitidan Samobitshi -> 3")
print ("Samobitidan Atobitshi -> 4")
print ("Atobitidan Otxobitshi -> 5")
print ("Otxobitidan Atobitshi -> 6")
print ("Atobitidan Rvaobitshi -> 7")
print ("Rvaobitidan Atobitshi -> 8")
print ("Atobitidan Tekvsmetobitshi -> 9")
print ("Tekvsmetobitidan Atobitshi -> 10")


while True :

    userinput=int(input())

    ans=""
    ans1=0
    
    if userinput==1 :
        a=int(input())
        while a!=0 :
            ans=str(a%2)+ans
            a//=2
        print(ans)

    elif userinput==2 :
        a=input()
        al=len(a)
        for i in range (al-1,-1,-1) :
            ans1+=int(a[i])*(pow(2,al-1-i))
        print(ans1)

    elif userinput==3 :
        a=int(input())
        while a!=0 :
            ans=str(a%3)+ans
            a//=3
        print(ans)

    elif userinput==4 :
        a=input()
        al=len(a)
        for i in range (al-1,-1,-1) :
            ans1+=int(a[i])*(pow(3,al-1-i))
        print(ans1)
    
    elif userinput==5 :
        a=int(input())
        while a!=0 :
            ans=str(a%4)+ans
            a//=4
        print(ans)
    
    elif userinput==6 :
        a=input()
        al=len(a)
        for i in range (al-1,-1,-1) :
            ans1+=int(a[i])*(pow(4,al-1-i))
        print(ans1)

    elif userinput==7 :
        a=int(input())
        while a!=0 :
            ans=str(a%8)+ans
            a//=8
        print(ans)

    elif userinput==8 :
        a=input()
        al=len(a)
        for i in range (al-1,-1,-1) :
            ans1+=int(a[i])*(pow(8,al-1-i))
        print(ans1)    

    elif userinput==9 :
        a=int(input())
        while a!=0 :
            c=a%16
            char=''
            if c>9 :
                if c==10 :
                    char='A'
                if c==11 :
                    char='B'
                if c==12 :
                    char='C'
                if c==13 :
                    char='D'
                if c==14 :
                    char='E'
                if c==15 :
                    char='F'
                ans=char+ans
            else :
                ans=str(a%16)+ans
            a//=16
        print(ans)
    
    elif(userinput==10) :
        a=str(input())
        al=len(a)
        c=0
        for i in range (al-1,-1,-1) :
            if a[i]>='A' and a[i]<='G' :
                char=a[i]
                if char=='A':
                    c=10
                if char=='B' :
                    c=11
                if char=='C' :
                    c=12
                if char=='D' :
                    c=13
                if char=='E' :
                    c=14
                if char=='F' :
                    c=15
                ans1+=c*(pow(16,al-1-i))
            else :
                ans1+=int(a[i])*pow(16,al-i-1)    
        print(ans1)  
        