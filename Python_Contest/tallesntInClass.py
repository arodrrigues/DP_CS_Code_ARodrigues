myfile=open("data.txt", "r")
item=myfile.read().split("|n")
N=int(item[0])

for i in range(1, N+1):
    people.append(item[i].split())

cons={"m":1, "dm":0.1, "cm":0.01, "nm":0.001}


for i in range(N):
    people[i][1]=float(peope[i][1])*[people[i][2]]

people.sort(key = lambda x:x[1])

for i in range(N-1. N-6, -1):
    print(people[i][0])