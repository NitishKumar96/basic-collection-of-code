# Toggel string // 18 feb 2017 // python 3

''' code monk tutorial basics
in this we have to change the case of the input string
size limit 5 mb
time limit 5 sec '''

# solution 1

var= input()                                     # take input string
out=''                                           # declare a string for the further use
for i in range (0,len(var)):                     # for loop to select each cahrector one by one
    cal=var[i]                                   # select one variable
    if cal.islower():                            # check the case
        cal=cal.upper()                          # change the case
    elif cal.isupper():
        cal=cal.lower()
    out+=cal                                     # add the final output in a string
print (out)                                      # give the final output

# solution 2
# cocept is same as the 1 only the code is different

S=raw_input()
text=[]
text=list(S)

for x,key in enumerate(text):
	if key.isupper():
		text[x]=key.lower()
	else:
		text[x]=key.upper()

M="".join(text)
