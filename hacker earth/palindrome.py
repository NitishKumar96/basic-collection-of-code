# code to check the palindrome

#solution 1
string=input()
i=int ((len(string)/2))
if len(string)%2==0 :
    i=int(len(string)/2)
    if string[0:i]== string[i:2*i+2][::-1]:
        print('yes')
    else: print('no')
else:
    i=int(len(string)/2-0.5)
    if string[0:i]== string[i+1:2*i+1][::-1]:
        print('yes')
    else: print('no')


#solution 2
a = raw_input()
la = len(a)/2
flag = 0
for i in range(la):
    if a[:i+1] == a[-(i+1):]:
    	flag = 1
print ('YES' if flag else 'NO')

#solution 3 similar to solution 1
S=input()
end=len(S)-1
status= 'YES'
i=0
while i-end<=0:
    if S[i]!=S[end]:
        status='NO'
    i+=1
    end-=1
print( status)
