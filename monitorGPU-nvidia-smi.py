import os
import re
import time

# 获取显存使用情况
def parseGPUMem(str_content):
    lines = str_content.split("\n")
    target_line = lines[9]
    mem_part = target_line.split("|")[2]
    use_mem = mem_part.split("/")[0]
    total_mem = mem_part.split("/")[1]
    use_mem_int = int(re.sub("\D", "", use_mem))
    total_mem_int = int(re.sub("\D", "", total_mem))
    return use_mem_int, total_mem_int

# 获取GPU使用情况
def parseGPUUseage(str_content):
    lines = str_content.split("\n")
    target_line = lines[9]
    useage_part = int(target_line.split("|")[3].split("%")[0])
    return useage_part


fout = open("GPUlog.txt", "w")
fout.write("# timestamp(sec), total gpu memory(GB), used gpu memory(GB), GPU percent\n")

while True:
    str_command = "nvidia-smi"
    out = os.popen(str_command)
    cur_time = time.time()
    text_content = out.read()
    out.close()

    used_mem, total_mem = parseGPUMem(text_content)
    use_percent = parseGPUUseage(text_content)
    print("used memory:", used_mem/1024.0, "GB","percnet:", use_percent)
    fout.write(str(cur_time)+","+str(total_mem/1024.0)+","+str(used_mem/1024.0)+","+str(use_percent)+"\n")

    time.sleep(0.5)

fout.close()