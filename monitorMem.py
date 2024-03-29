import psutil
import time


GB = 1024*1024*1024

fout = open("./MEMlog.txt", "w")

tip_content = "#timestamp(sec), total memory(GB), used memory(GB), percent, total swap memory(GB), used swap memory(GB), percent\n"
fout.write(tip_content)

while True:
    # 返回内存
    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()
    cur_time = time.time()

    vm_total = vm.total/GB
    vm_used = vm.used/GB
    vm_percent = vm.percent
    sm_total = sm.total/GB
    sm_used = sm.used/GB
    sm_percent = sm.percent
    fout.write(str(cur_time)+","+str(vm_total)+","+str(vm_used)+","+str(vm_percent)+","+str(sm_total)+","+str(sm_used)+","+str(sm_percent)+"\n")
    print(str(cur_time)+":"+str(vm_used)+"GB/"+str(vm_total)+"GB", str(vm_percent)+"%")
    time.sleep(0.5)

fout.close()