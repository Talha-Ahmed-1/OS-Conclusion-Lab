# from numpy import*
# from array import *

sequence=[]

class Process:
    def __init__(self,id,AT,BT):
        self.id = id
        self.AT = AT
        self.burst = BT

def SJF(check,num,nump):
    global sequence
    queue=[]
    time = 0
    ap=0
    rp=0
    done=0

    if True:
        while (done < num):
            for i in range(ap, num):
                if time >= check[i].AT:
                    queue.append(check[i])
                    ap += 1
                    rp += 1

            if rp < 1:
                time += 1
                sequence.append(0)
                # continue
            queue.sort(key=lambda x: (x.burst))
            if queue[0].burst > 0:
                    sequence.append(queue[0].id)
                    time += 1
                    queue[0].burst -=1
                    if(queue[0].burst<1):
                        queue[0].burst = 99
                        done += 1
                        rp -= 1

ct=[]
final=[]

data = [
    [1,0,24],
    [2,1,5],
    [3,2,10],
    [4,3,8]
]

processes = len(data)


for i in range(0,processes):
    final.append(Process(data[i][0],data[i][1],data[i][2]))


SJF(final,len(final),1)


for i in range(0,processes):
    ct.append([])



for i in range(0,processes):
    for j in range(0,len(sequence)):
        if(i+1==sequence[j]):
            ct[i]=j+1

# print('CT')
# print(ct)
P="Process"
AT="Arrival Time"
BT="Brust Time"
CT="Calculated Time"
TAT="Turned Arround Time"
WT="Waiting Time"
h=0
print("%-15s %-15s %-15s %-15s %-15s %-15s " %(P,AT,BT,CT,TAT,WT))
for i in range(0,processes):
    print("P%-17s %-17s %-17s %-17s %-17s %-17s" %(data[i][0],data[i][1],data[i][2],ct[i],(ct[i]-data[i][1]),((ct[i]-data[i][1])-data[i][2])))
print("Gantt sequence")
print(len(sequence))