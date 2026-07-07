import shutil
import psutil
from datetime import datetime

print(f"Time={datetime.now()}")

print(f"CPU_Usage={psutil.cpu_percent(interval=1)}%")

memory = psutil.virtual_memory()
print(f"Memory_Usage={memory.percent}%")

disk = shutil.disk_usage("/")

disk_used = (disk.used / disk.total) * 100
print(f"Disk_Usage={disk_used:.1f}%")