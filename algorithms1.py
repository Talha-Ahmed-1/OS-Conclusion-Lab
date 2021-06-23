from prettytable import PrettyTable
import copy
def FCFS():
    processes = [0 for x in range(int(input("Enter no. of processes: ")))]
    t = PrettyTable(['Process', 'Burst Time', 'Waiting Time', 'Turn Around Time'])
    for i in range(len(processes)):
        proc = "P"+str(i)
        print("Enter burst time of",proc,":")
        processes[i] = int(input())

    turnTime = 0
    waitingTime = 0
    tt = 0
    tw = 0


    count = 1
    for i in processes:
        turnTime += i
        tw += waitingTime
        tt += turnTime
        t.add_row(["P"+str(count),i,waitingTime,turnTime])
        count += 1
        waitingTime += i 
    print(t)
    print("Average Waiting Time: ", tw/len(processes))
    print("Average Turn Around Time: ", tt/len(processes))
def RR():
    t = 0
    bt = [0 for x in range(int(input("Enter no. of processes: ")))]
    for i in range(len(bt)):
        proc = "P"+str(i)
        print("Enter burst time of",proc,":")
        bt[i] = int(input())
    ct = [0]*len(bt)
    quantum = int(input("Input Quantum: "))
    wt = ct.copy()
    rem_bt = bt.copy()

    table = PrettyTable(['Process', 'Burst Time', 'Waiting Time', 'Turn Around Time'])

    while True:
        flag = True
        for i in range(len(bt)):
            if rem_bt[i] > 0:
                if rem_bt[i] > quantum:
                    wt[i] += quantum
                    t += quantum
                    rem_bt[i] -= quantum
                    flag = False
                else:
                    if wt[i] != 0:
                        wt[i] = t - wt[i]
                    else:
                        wt[i] += t
                    t += rem_bt[i]
                    ct[i] = t
                    rem_bt[i] = 0
        if flag:
            break
    for i in range(len(bt)):
        table.add_row([i,bt[i],wt[i],ct[i]])
    print(table)
    print("Average waiting time :", sum(wt)/len(bt))
    print("Average turn around time: ", sum(ct)/len(bt))
def Priority():
    processes = [0 for x in range(int(input("Enter no. of processes: ")))]
    for i in range(len(processes)):
        proc = "P"+str(i)
        print("Enter burst time of",proc,":")
        processes[i] = int(input())
    t = PrettyTable(['Process', "Priority", 'Burst Time', 'Waiting Time', 'Turn Around Time'])

    priority = [0 for x in range(len(processes))]
    for i in range(len(processes)):
        proc = "P"+str(i)
        print("Enter priority of",proc,":")
        priority[i] = int(input())
    processNo = [x for x in range(0,len(processes))]
    def bubbleSort(arr,process,processN): 
        n = len(arr) 
        for i in range(n): 
            for j in range(0, n-i-1): 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    process[j], process[j+1] = process[j+1], process[j]
                    processN[j], processN[j+1] = processN[j+1], processN[j]

    bubbleSort(priority,processes,processNo)


    turnTime = 0
    waitingTime = 0
    tt = 0
    tw = 0

    count = 0
    for i in processes:
        turnTime += i
        tw += waitingTime
        tt += turnTime
        t.add_row(["P"+str(processNo[count]),priority[count],i,waitingTime,turnTime])
        count += 1
        waitingTime += i 
    print(t)
    print("Average Waiting Time: ", tw/len(processes))
    print("Average Turn Around Time: ", tt/len(processes)) 
def SJF():
    processes = [0 for x in range(int(input("Enter no. of processes: ")))]
    t = PrettyTable(['Process', 'Burst Time', 'Waiting Time', 'Turn Around Time'])
    for i in range(len(processes)):
      proc = "P"+str(i)
      print("Enter burst time of",proc,":")
      processes[i] = int(input())
    
    processNo = [x for x in range(0,len(processes))]
    def bubbleSort(arr,process): 
        n = len(arr) 
        for i in range(n): 
            for j in range(0, n-i-1): 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    process[j], process[j+1] = process[j+1], process[j]

    bubbleSort(processes,processNo)


    turnTime = 0
    waitingTime = 0
    tt = 0
    tw = 0

    count = 0
    for i in processes:
        turnTime += i
        tw += waitingTime
        tt += turnTime
        t.add_row(["P"+str(processNo[count]),i,waitingTime,turnTime])
        count += 1
        waitingTime += i 
    print(t)
    print("Average Waiting Time: ", tw/len(processes))
    print("Average Turn Around Time: ", tt/len(processes)) 
def main():
    get = int(input("1: SJF\n2: Priority\n3: Round Robin\n4: FCFS\n"))
    if get == 1:
        SJF()
    elif get == 2:
        Priority()
    elif get == 3:
        RR()
    elif get == 4:
        FCFS()
    else:
        exit(1)
main()