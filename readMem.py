import psutil

GB = 1024*1024*1024

# 返回内存
vm = psutil.virtual_memory()
vm_total = vm.total/GB
print("total memory(GB):", vm_total)

# 返回交换内存
sm = psutil.swap_memory()
sm_total = sm.total/GB
print("swap memory(GB):", sm_total)