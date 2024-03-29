import platform

fout = open("info_platform.txt", "w")

# 返回平台架构
arch = platform.architecture()
arch_str = "architecture:"+str(arch)+"\n"
fout.write(arch_str)
print(arch_str)

# 返回平台CPU型号
cpu = platform.processor()
cpu_str = "cpu:"+cpu+"\n"
fout.write(cpu_str)
print(cpu_str)

# 返回平台型号
mcn = platform.machine()
mcn_str = "machine:"+mcn+"\n"
fout.write(mcn_str)
print(mcn_str)

# 返回平台系统名称
plm = platform.platform()
plm_str = "platform:"+plm+"\n"
fout.write(plm_str)
print(plm_str)

# 返回平台系统类型
sys = platform.system()
sys_str = "system:"+sys+"\n"
fout.write(sys_str)
print(sys_str)

# 返回系统精确版本
ver = platform.version()
ver_str = "version:"+ver+"\n"
fout.write(ver_str)
print(ver_str)

# 返回平台网络名称
node = platform.node()
node_str = "node:"+node+"\n"
fout.write(node_str)
print(node_str)

# 返回系统详细信息
uname = platform.uname()
uname_str = "uname:"+str(uname)+"\n"
fout.write(uname_str)
print(uname_str)

fout.close()