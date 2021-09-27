import re
import os

f = open("./trace.log")
timestamp = re.compile('\d{1,9}\.\d{6}')
pid = re.compile('-\d{1,}')
next_pid = re.compile('next_pid=\d{1,}')
pre_pid = re.compile('prev_pid=\d{1,}')
count = -1
for count, line in enumerate(f.readlines()):
    count += 1
print("行数：", count)

n = 1
for i in range(0, count - 1, 1):
    f.seek(0)
    lines = f.readlines()
    line = lines[n]
    print(n, line)
    
    if line.find('sched_wakeup:') != -1:  
        time_wakeup = timestamp.search(line)
        pid_wakeup = pid.search(line)
        print("sched_wakeup:", "PID", pid_wakeup.group(), "TIMESTAMP", time_wakeup.group())
        
        m = n + 1
        for o in range(0, count - 1 - n, 1):
            f.seek(0)
            linem = f.readlines()[m]  

            print("#######", m, linem)
            if linem.find('sched_switch:') != -1:  
                prev_pid = "prev_pid=" + pid_wakeup.group()[1:]
                if linem.find(prev_pid) != -1:  
                    time_switch = timestamp.search(linem)  
                    print("sched_switch：", "PID", pid_wakeup.group(), "TIMESTAMP", time_switch.group())
                    print("\n\n")
                    print("@@@@@@sched_latency for PID", pid_wakeup.group(), "latency=[timeB-timeA]=[",
                          time_switch.group(), "-", time_wakeup.group(), "]=",
                          float(time_switch.group()) - float(time_wakeup.group()), " wakeup=timeA switch=timeB")
                    print("\n\n")

                    break
            m += 1
            
    if line.find('sched_wakeup_new:') != -1:  
        time_wakeup = timestamp.search(line)
        pid_wakeup = pid.search(line)
        print("sched_wakeup:", "PID", pid_wakeup.group(), "TIMESTAMP", time_wakeup.group())
        
        m = n + 1
        for o in range(0, count - 1 - n, 1):
            f.seek(0)
            linem = f.readlines()[m]  

            print("#######", m, linem)
            if linem.find('sched_switch:') != -1:  
                prev_pid = "prev_pid=" + pid_wakeup.group()[1:]
                if linem.find(prev_pid) != -1:  
                    time_switch = timestamp.search(linem)  
                    print("sched_switch：", "PID", pid_wakeup.group(), "TIMESTAMP", time_switch.group())
                    print("\n\n")
                    print("@@@@@@sched_latency for PID", pid_wakeup.group(), "latency=[timeB-timeA]=[",
                          time_switch.group(), "-", time_wakeup.group(), "]=",
                          float(time_switch.group()) - float(time_wakeup.group()), " wakeup=timeA switch=timeB")
                    print("\n\n")

                    break
            m += 1
            
    if line.find('sched_switch:') != -1:  
        time_wakeup = timestamp.search(line)
        pid_wakeup = pid.search(line)
        switch_nextpid = next_pid.search(line)  
        print("sched_switch：", "PID", pid_wakeup.group(), "TIMESTAMP", time_wakeup.group(), "next_pid",
              switch_nextpid.group())
        
        m = n + 1
        for o in range(0, count - 1 - n, 1):
            f.seek(0)
            linem = f.readlines()[m]  

            print("?????", m, linem)
            if linem.find('sched_switch:') != -1:  

                switch_prev_pid = pre_pid.search(linem)  

                if switch_prev_pid.group()[4:] == switch_nextpid.group()[4:]:  
                    time_switch = timestamp.search(linem)  
                    print("sched_switch：", "PID", pid_wakeup.group(), "TIMESTAMP", time_switch.group(), "prev_pid",
                          switch_prev_pid.group())
                    print("\n\n")
                    print("@@@@@@sched_latency for PID", pid_wakeup.group(), "latency=[timeB-timeA]=[",
                          time_switch.group(), "-", time_wakeup.group(), "]=",
                          float(time_switch.group()) - float(time_wakeup.group()), " wakeup=timeA switch=timeB")
                    print("\n\n")

                    break
                else:
                    break
            m += 1

    n += 1  
print("over！")  
f.close()







