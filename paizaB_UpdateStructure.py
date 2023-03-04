# coding: utf-8
# Your code here!
ninzu,kousinsu=map(int,input().split())
#print(kousinsu) 1  1

status=[0]*ninzu
status_kousin=[0]*kousinsu
for i in range(ninzu):
    status[i] = input().split()
#print(status)#[['koko', '23', '04/10', 'tokyo']]
for a in range(kousinsu):
    status_kousin[a] = input().split()
#print(status_kousin)
for b in status_kousin:
    #print(b)
    for c in range(len(status)):
        if c==int(b[0])-1:
            status[c][0]=b[1]
print(status)
