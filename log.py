
def read_log_file(filename):
    """Reads the log file and returns lines"""

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            if not lines:
                print("Log file is empty")
                return None

            return lines

    except FileNotFoundError:
        print("Error: Log file not found")
        return None


def count_log_levels(lines):
    """Counts INFO, WARNING and ERROR"""

    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in lines:
        if "INFO" in line:
            log_counts["INFO"] += 1
        elif "WARNING" in line:
            log_counts["WARNING"] += 1
        elif "ERROR" in line:
            log_counts["ERROR"] += 1

    return log_counts


def print_summary(counts):
    """Print summary to terminal"""

    print("\n===== Log Summary =====")
    print(f"INFO messages    : {counts['INFO']}")
    print(f"WARNING messages : {counts['WARNING']}")
    print(f"ERROR messages   : {counts['ERROR']}")


def write_summary_to_file(counts):
    """Writes summary to file"""

    with open("log_summary.txt", "w") as file:
        file.write("Log Analysis Summary\n")
        file.write("----------------------\n")
        file.write(f"INFO    : {counts['INFO']}\n")
        file.write(f"WARNING : {counts['WARNING']}\n")
        file.write(f"ERROR   : {counts['ERROR']}\n")

    print("\nSummary written to log_summary.txt")


def main():
    filename = "app.log"

    lines = read_log_file(filename)

    if lines is None:
        return

    counts = count_log_levels(lines)

    print_summary(counts)
    write_summary_to_file(counts)



main()
