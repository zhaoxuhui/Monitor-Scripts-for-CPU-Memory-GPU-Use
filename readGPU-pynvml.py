import pynvml

# 初始化 pynvml
pynvml.nvmlInit()

# 获取 GPU 数量
deviceCount = pynvml.nvmlDeviceGetCount()
print("GPU number:", pynvml.nvmlDeviceGetCount())

# 获取GPU信息
for i in range(deviceCount):
   handle = pynvml.nvmlDeviceGetHandleByIndex(i)
   
   
   gpu_name = pynvml.nvmlDeviceGetName(handle)
   print("GPU name:", gpu_name)

   mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
   print("GPU Memory:", mem_info.total/(1024*1024*1024),"GB")


# 清理和释放资源
pynvml.nvmlShutdown()