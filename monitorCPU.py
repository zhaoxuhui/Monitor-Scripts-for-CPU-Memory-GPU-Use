import platform
import psutil
import time
import numpy as np

# 返回平台CPU型号
cpu = platform.processor()
cpu_str = "cpu:"+cpu
print(cpu_str)

# 返回平台CPU逻辑和物理核心数
core_num_logical = psutil.cpu_count()
core_num_physical = psutil.cpu_count(logical=False)
print("logical core:", core_num_logical)
print("physical core:", core_num_physical)

# 启动记录
fout = open("CPUlog.txt", "w")
fout.write(cpu_str+"\n")
fout.write("logical core:" + str(core_num_logical) + "\n")
fout.write("physical core:" + str(core_num_physical) + "\n")
tip_content = "#timestamp(sec), mean cpu percent"
for i in range(core_num_logical):
    tip_content += ", core_"+str(i)
tip_content += "\n"
fout.write(tip_content)

while True:
    cur_stats = psutil.cpu_percent(interval=0.5, percpu=True)
    cur_time = time.time()
    mean_stats = np.mean(cur_stats)
    fout.write(str(cur_time)+","+str(mean_stats))
    for i in range(len(cur_stats)):
        fout.write(","+str(cur_stats[i]))
    fout.write("\n")
    print(cur_time, mean_stats, cur_stats)

fout.close()
