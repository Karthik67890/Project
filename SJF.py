
p = [[]]*8
p[0] = [4,24,5,73,3,31,5,27,4,33,6,43,4,64,5,19,2]
p[1] = [18,31,19,35,11,42,18,43,19,47,18,43,17,51,19,32,10]
p[2] = [6,18,4,21,7,19,4,16,5,29,7,21,8,22,6,24,5]
p[3] = [17,42,19,55,20,54,17,52,15,67,12,72,15,56,14]
p[4] = [5,81,4,82,5,71,3,61,5,62,4,51,3,77,4,61,3,42,5]
p[5] = [10,35,12,41,14,33,11,32,15,41,13,29,11]
p[6] = [21,51,23,53,24,61,22,31,21,43,20]
p[7] = [11,52,14,42,15,31,17,21,16,43,12,31,13,32,15]

def burst(t):
    options = {
        0 :cpu,
        1 :io
    }

options[t]()

def cpu_burst(n):
    for x in range(n):
        burst(0)

def io_burst(n):
    for x in range(n):
        burst(1)

def analysis(ps):
totcpu = []
totio = []
tot = []
for x in range(len(ps)):
    tempsum_cpu = 0
    tempsum_io = 0
    #print(x, " P~~~~~~~~~~~~~~~~~~~~~~~~~")
    for y in range(1,len(p[x]),2):
        tempsum_cpu += p[x][y-1]
        tempsum_io += p[x][y]
    totcpu.append(tempsum_cpu)
    totio.append(tempsum_io)
    tot.append(tempsum_cpu + tempsum_io)

tcpu = totcpu[:]
tio = totio[:]
ttot = tot[:]
ordercpu = []
orderio = []
ordertot = []
for x in range(len(ps)):
    ordercpu.append(tcpu.index(min(tcpu)))
    tcpu[tcpu.index(min(tcpu))] = 9999
    orderio.append(tio.index(min(tio)))
    tio[tio.index(min(tio))] = 9999
    ordertot.append(ttot.index(min(ttot)))
    ttot[ttot.index(min(ttot))] = 9999

#print(ordercpu,"\n",orderio,"\n",ordertot)



return ordertot




def sjf(ps):
a = analysis(ps)

totcputime = 0
totiotime = 0
totaltime = 0

readyq = []
waitingtime = 0
waitingtimes = []


for x in a:
    l = len(ps[x])
    processstart = time.time()
    procputime = 0
    prociotime = 0
    bc = 0    
    print("================================================")
    for i in range(0,l-2,2):
        bc+=1
        cs = time.time()
        cpu_burst(ps[x][i])
        ce = time.time()
        cdur = (ce - cs)
        procputime += cdur
        print("|| --CPU Burst",bc," BurstDuration:",end='')
        print("%8.6f" % cdur,"s    ||")

        ios = time.time()
        io_burst(ps[x][i+1])
        ioe = time.time()
        iodur = (ioe - ios)
        prociotime += iodur
        print("|| **IO Time:%8.6f" % iodur,"s                       ||")

    readyq.append(x)

    processend = time.time()
    procduration = (processend - processstart)
    print("||vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv||")
    print("||   Process #",x+1,"                             ||")
    print("||   Process CPU Burst Time:%8.6f" % (procputime),"s        ||")
    print("||   Process IO Time:%8.6f" % (prociotime),"s               ||")
    print("||   Time waiting:%8.6f" % (waitingtime),"s                  ||")
    print("||   TOTAL PROCESS TIME:%8.6f" % (procduration),"s            ||")
    print("================================================")

    totcputime += procputime
    totiotime += prociotime
    totaltime += procduration

    waitingtimes.append(waitingtime)
    waitingtime += procputime

    ###################################333

print("*************************************")
print("***   Scheduler Time:%8.6f" % (totaltime),"s   ***")
print("***   CPU Burst Time:%8.6f" % (totcputime),"s   ***")
print("***   IO Time:%8.6f" % totiotime,"s          ***")
print("*************************************")

#sjf(p)
def fcfs(ps):
    total_duration = 0

    tot_iotime = 0
    tot_cputime = 0
    ss = time.time()
    for x in range(8):
            #print("**************************")
            #print("***        Process ", x+1, " ***")
            #print("**************************")


            print("================================================")
            y = 0
            s = time.time()
            bc = 0
            while y < len(p[x])-2:

                    bc += 1
                    print("|| --CPU Burst",bc," BurstDuration:",end='')

                    sb = time.time()
                    cpu_burst(p[x][y])
                    eb = time.time()
                    bt = (eb - sb)
                    tot_cputime += bt
                    print("%8.6f" % bt,"s    ||")

                    sio = time.time()
                    io_burst(p[x][y+1])
                    eio = time.time()
                    io_time = (eio - sio)
                    tot_iotime += io_time
                    print("|| **IO Time:%8.6f" % io_time,"s                       ||")

                    y += 2
            e = time.time()
            processtime = (e-s)
            total_duration += processtime
            print("||vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv||")
            print("||   Process #",x+1,"                             ||")
            print("||   Process CPU Burst Time:%8.6f" % (tot_cputime),"s        ||")
            print("||   Process IO Time:%8.6f" % (tot_iotime),"s               ||")
            #print("||   Time waiting:%8.6f" % (waitingtime),"s             ||")
            print("||   TOTAL PROCESS TIME:%8.6f" % (processtime),"s            ||")
            print("================================================")

            #print("Process duration:",processtime)
    se = time.time()
    schedulerTime = (se - ss)
    '''
    print("********************************************")
    print("*** SchdulerTime:",schedulerTime,"s")
    print("*** Total I/O Time:",tot_iotime,"s")
    print("*** Total CPU Time:",tot_cputime,"s")
    print("********************************************")
    '''
    print("*************************************")
    print("***   Scheduler Time:%8.6f" % (schedulerTime),"s   ***")
    print("***   CPU Burst Time:%8.6f" % (tot_cputime),"s   ***")
    print("***   IO Time:%8.6f" % tot_iotime,"s          ***")
    print("*************************************")
