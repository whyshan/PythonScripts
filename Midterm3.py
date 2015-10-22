num = 1
numlist = []

while num != 0:
    num = int(raw_input('next num: '))
    numlist.append(num)
numlist.pop()
numlist.sort()

newnum = int(raw_input('new num: '))
done = 0
cnt = 0
while not done and cnt < len(numlist):
    if newnum < numlist[cnt]:
        numlist.insert(cnt, newnum)
        done = 1
    cnt+=1
if not done:
    numlist.append(newnum)

print numlist 
