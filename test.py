from ctypes import *
import os
os.system("echo 0 > /sys/kernel/debug/tracing/options/function-trace") 
os.system("echo function > /sys/kernel/debug/tracing/current_tracer")
os.system("echo 1 > /sys/kernel/debug/tracing/tracing_on")
os.system("echo 0 > /sys/kernel/debug/tracing/tracing_max_latency")
adder = CDLL('./test.so')
adder.main()
os.system("echo 0 > /sys/kernel/debug/tracing/tracing_on")
os.system("cat /sys/kernel/debug/tracing/trace")

