from ctypes import *
import os
os.system("echo 0 > /sys/kernel/debug/tracing/tracing_on")
os.system("echo  > /sys/kernel/debug/tracing/trace")
os.system("echo 0 > /sys/kernel/debug/tracing/options/function-trace") 
os.system("echo sched:sched_stat_runtime > /sys/kernel/debug/tracing/set_event")
os.system("echo 1 >  /sys/kernel/debug/tracing/events/sched/enable") 
os.system("echo 1 > /sys/kernel/debug/tracing/tracing_on")
os.system("echo 0 > /sys/kernel/debug/tracing/tracing_max_latency")
adder = CDLL('./test.so')
adder.main()
os.system("echo 0 > /sys/kernel/debug/tracing/tracing_on")
os.system("cat /sys/kernel/debug/tracing/trace")

