import time
import pynvml

fout = open("GPUlog.txt", "w")
fout.write("# timestamp(sec), total gpu memory(GB), used gpu memory(GB), GPU percent\n")

# 初始化 pynvml
pynvml.nvmlInit()

# 获取 GPU 数量
deviceCount = pynvml.nvmlDeviceGetCount()
print("GPU number:", pynvml.nvmlDeviceGetCount())

handle = pynvml.nvmlDeviceGetHandleByIndex(0)

while True:
   mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
   gpu_info = pynvml.nvmlDeviceGetUtilizationRates(handle)
   cur_time = time.time()

   mem_used = mem_info.used/(1024*1024*1024)
   mem_total = mem_info.total/(1024*1024*1024)
   gpu_percent = gpu_info.gpu

   print("used memory:", mem_used, "GB","percnet:", gpu_percent)
   fout.write(str(cur_time)+","+str(mem_total)+","+str(mem_used)+","+str(gpu_percent)+"\n")

   time.sleep(0.5)

# 清理和释放资源
pynvml.nvmlShutdown()
fout.close()