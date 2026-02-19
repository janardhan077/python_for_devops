class LogAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.logs = []
        self.error_count = 0
        self.warning_count = 0
        self.info_count = 0

    def load_logs(self):
        try:
            with open(self.file_path, "r") as file:
                self.logs = file.readlines()
            print("Logs loaded successfully\n")
        except FileNotFoundError:
            print("Log file not found!")

    def analyze_logs(self):
        for line in self.logs:
            line = line.lower()

            if "error" in line:
                self.error_count += 1
            elif "warning" in line:
                self.warning_count += 1
            elif "info" in line:
                self.info_count += 1

    def show_summary(self):
        print("----- LOG SUMMARY -----")
        print("Errors  :", self.error_count)
        print("Warnings:", self.warning_count)
        print("Info    :", self.info_count)


if __name__ == "__main__":
    analyzer = LogAnalyzer("day04.log")
    analyzer.load_logs()
    analyzer.analyze_logs()
    analyzer.show_summary()
