# ******************************
# Make your Code
# ****************************
inputvalues=input("All names:")
names1=inputvalues.split()
shortest="zooooooooooooooooooooooooooooooooooooo"
longest="a"
x=0
while x<len(names1):
    if len(shortest)>=len(names1[x]) and ord(shortest[0])>ord(names1[x][0]):
        shortest=names1[x]
    if len(shortest)>len(names1[x]):
        shortest=names1[x]
    if len(longest)<=len(names1[x]) and ord(longest[0])<ord(names1[x][0]):
        longest=names1[x]
    if len(longest)<len(names1[x]):
        longest=names1[x]
    x=x+1
print(shortest, longest)