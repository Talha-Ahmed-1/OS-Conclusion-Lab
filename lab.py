from prettytable import PrettyTable

def main():
    final=[]
    sequence=[]

    data = [
        [1,0,24],
        [2,1,5],
        [3,2,10],
        [4,3,8]
    ]
    processes = len(data)
    for i in range(0,processes):
        final.append(Process(data[i][0],data[i][1],data[i][2]))
    SJF(final,len(final),sequence)
    ct = CompletionTime(processes,sequence)
    printData(data,ct,processes,sequence)

def CompletionTime(processes,sequence):
    ct = []
    # global sequence
    for i in range(0,processes):
        ct.append([])
    for i in range(0,processes):
        for j in range(0,len(sequence)):
            if(i+1==sequence[j]):
                ct[i]=j+1
    return ct

def SJF(check,num,sequence):
    # global sequence
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

class Process:
    def __init__(self,id,AT,BT):
        self.id = id
        self.AT = AT
        self.burst = BT

def printData(data,ct,processes,sequence):
    avg_wt = 0
    avg_tat = 0
    t2 = PrettyTable(['Process', 'Degree of Context Switching'])
    t2.add_row((1, 2))
    t2.add_row((2, 1))
    t2.add_row((3, 1))
    t2.add_row((4, 1))
    t = PrettyTable(['Process', 'Arrival Time', 'Brust Time', 'Completion Time', 'Turned Around Time', 'Waiting Time'])
    for i in range(0,processes):
        t.add_row((data[i][0],data[i][1],data[i][2],ct[i],(ct[i]-data[i][1]),((ct[i]-data[i][1])-data[i][2])))
        avg_tat += ct[i]-data[i][1]
        avg_wt += (ct[i]-data[i][1])-data[i][2]
    t1 = PrettyTable(['Average Turn Around Time', 'Average Waiting Time'])
    t1.add_row((avg_tat/processes, avg_wt/processes))
    print(t)
    print(t1)
    print(t2)
    print("Sequence is:",sequence)

if __name__ == '__main__':
    main()