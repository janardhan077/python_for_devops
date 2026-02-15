import psutil
def status_show ( name , current ,thershold):
    if current < thershold :
        status = "ok"
    elif current >= thershold +10  :
        status = "WARNING"
    else :
        status = "CRITICAL"
    print (f"{name}usage :{current} % {status}")
cpu_thershold =int(input("enter the cpu_thershold :"))
disk_thershold =int(input("enter the disk thershold :"))
memory_thershold =int(input("enter the memory thershold :"))
current_cpu = psutil.cpu_percent(interval=1)
current_disk = psutil.disk_usage('/').percent
curent_memory = psutil.virtual_memory().percent
print("******************* here is your system health  *************************************")
status_show("cpu",current_cpu , cpu_thershold )
status_show ("disk",current_disk, disk_thershold)  
status_show ("memory" ,curent_memory,memory_thershold)      
