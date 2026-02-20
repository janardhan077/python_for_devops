import argparse
import os


class LogAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def analyze(self, level=None):
        summary = {}

        with open(self.file_path, "r") as file:
            for line in file:
                line = line.strip()

                if ":" in line:
                    log_level = line.split(":")[0]

                    if level and log_level != level:
                        continue

                    if log_level in summary:
                        summary[log_level] += 1
                    else:
                        summary[log_level] = 1

        return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Log file path")
    parser.add_argument("--out", help="Output file path")
    parser.add_argument("--level", help="Filter by log level (example: ERROR)")

    args = parser.parse_args()

    # Check if file exists
    if not os.path.exists(args.file):
        print("Error: File not found")
        return

    analyzer = LogAnalyzer(args.file)
    result = analyzer.analyze(args.level)

    print("\nLog Summary:")
    for key, value in result.items():
        print(key, ":", value)

    if args.out:
        with open(args.out, "w") as out_file:
            for key, value in result.items():
                out_file.write(f"{key}: {value}\n")

        print("Summary written to", args.out)


if __name__ == "__main__":
    main()
