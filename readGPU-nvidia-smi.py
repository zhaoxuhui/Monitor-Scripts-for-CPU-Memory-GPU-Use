import os

def parseSMIVersion(text_content):
    lines = text_content.split("\n")
    target_line = lines[2]
    parts = target_line.split("NVIDIA-SMI")[1].split("Driver Version:")
    smi_version = parts[0].strip()
    driver_version = parts[1].split("CUDA Version:")[0].strip()
    cuda_version = parts[1].split("CUDA Version:")[1].split("|")[0].strip()
    return smi_version, driver_version, cuda_version

str_command = "nvidia-smi"
out = os.popen(str_command)
text_content = out.read()
out.close()

smi_ver, driver_ver, cuda_ver = parseSMIVersion(text_content)
print("smi version", smi_ver)
print("driver version", driver_ver)
print("cuda driver", cuda_ver)