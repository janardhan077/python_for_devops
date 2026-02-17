def get_threshold():
    try:
        cpu = int(input("Enter CPU threshold: "))
        mem = int(input("Enter Memory threshold: "))
        disk = int(input("Enter Disk threshold: "))
        return cpu, mem, disk
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None


def check_health(cpu, mem, disk):
    if cpu > 80:
        print("WARNING: CPU usage high")
    else:
        print("CPU usage normal")

    if mem > 80:
        print("WARNING: Memory usage high")
    else:
        print("Memory usage normal")

    if disk > 80:
        print("WARNING: Disk usage high")
    else:
        print("Disk usage normal")


def main():
    values = get_threshold()

    if values is None:
        print("Exiting safely...")
        return

    cpu, mem, disk = values
    check_health(cpu, mem, disk)


main()
