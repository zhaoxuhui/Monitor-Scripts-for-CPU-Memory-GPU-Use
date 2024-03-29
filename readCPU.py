import platform
import psutil

# 返回平台CPU型号
cpu = platform.processor()
cpu_str = "cpu:"+cpu
print(cpu_str)

# 返回平台CPU逻辑和物理核心数
core_num_logical = psutil.cpu_count()
core_num_physical = psutil.cpu_count(logical=False)
print("logical core:", core_num_logical)
print("physical core:", core_num_physical)