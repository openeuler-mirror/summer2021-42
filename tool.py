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
print("/sys/kernel/debug/tracing/trace输出行数：",count)

n=1
print("PID              LATENCY                SCHED_A              TIME_A               SCHED_B              TIME_B")
print(" |                  |                     |                    |                    |                     |  ")
for i in range(0, count-1, 1):
    f.seek(0)
    lines=f.readlines()
    line = lines[n]
    
    
    if line.find('sched_wakeup:') != -1: 
        time_wakeup = timestamp.search(line)
        pid_wakeup = pid.search(line)
        
        m=n+1
        for o in range(0, count-1-n, 1):
            f.seek(0)
            linem = f.readlines()[m]
            
            if linem.find('sched_switch:') != -1:
                prev_pid = "prev_pid="+pid_wakeup.group()[1:]
                if linem.find(prev_pid) != -1:
                    time_switch = timestamp.search(linem)
                    
                    print(pid_wakeup.group()[1:].ljust(10),float(time_switch.group())-float(time_wakeup.group())," sched_wakeup ".center(20),time_wakeup.group().center(20),"sched_switch".center(20),time_switch.group().center(20) )
                    break
            m += 1   
    
    if line.find('sched_wakeup_new:') != -1: 
        time_wakeup = timestamp.search(line)
        pid_wakeup = pid.search(line)
        
        
        m=n+1
        for o in range(0, count-1-n, 1):
            f.seek(0)
            linem = f.readlines()[m]
            
            
            if linem.find('sched_switch:') != -1:
                prev_pid = "prev_pid="+pid_wakeup.group()[1:]
                if linem.find(prev_pid) != -1:
                    time_switch = timestamp.search(linem)
                    
                    
                    print(pid_wakeup.group()[1:].ljust(10),float(time_switch.group())-float(time_wakeup.group())," sched_wakeup_new ".center(20),time_wakeup.group().center(20),"sched_switch".center(20),time_switch.group().center(20) )
                    
                
                    break
            m += 1   
    
    if line.find('sched_switch:') != -1: 
        time_wakeup = timestamp.search(line)
        pid_wakeup = pid.search(line)
        switch_nextpid = next_pid.search(line)
        
        
        m=n+1
        for o in range(0, count-1-n, 1):
            f.seek(0)
            linem = f.readlines()[m]
            
            
            if linem .find('sched_switch:') != -1:
                
                switch_prev_pid = pre_pid.search(linem)

                if switch_prev_pid.group()[4:] == switch_nextpid.group()[4:] :
                    time_switch = timestamp.search(linem)
                    
                    
                    print(pid_wakeup.group()[1:].ljust(10),float(time_switch.group())-float(time_wakeup.group())," sched_switch".center(20),time_wakeup.group().center(20),"sched_switch".center(20),time_switch.group().center(20) )
                    
                
                    break
                else:
                     break
            m += 1            
              
    n += 1
print("over！")
f.close()






