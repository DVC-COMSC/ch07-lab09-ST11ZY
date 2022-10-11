# ******************************
# Make your Code
# ****************************
inputvalues=input("All names:")
names1=inputvalues.split()
shortest="zooooooooooooooooooooooooooooooooooooo"
longest="a"
x=0
while x<len(names1):
    if len(shortest)>=len(names1[x]):
        shortest1=names1[x]
    if ord(shortest[0])>ord(shortest1[0]):
        shortest=shortest1
    if len(longest)<len(names1[x]):
        longest1=names1[x]
    if ord(longest[0])<ord(longest1[0]):
        longest=longest1
    x=x+1
print(shortest, longest)