import subprocess
from argparse import ArgumentParser
from tests.BaseTest import BaseTest


def parse_args():
    parser = ArgumentParser(description="Test Runner")
    parser.add_argument("-b", "--browser", default="chrome", help="Choose Browser")
    parser.add_argument("-v", "--verbose", default="True", help="Enable Verbose")
    parser.add_argument("-r", "--report", default="True", help="Report Generation")
    parser.add_argument("-n", "--parallel", default="True", help="For parallel execution")
    return parser.parse_args()


def run_tests(args):
    base = BaseTest()
    pytest_command = ["pytest"]

    if args.browser:
        pytest_command.append('--browser=chrome')

    if args.verbose:
        pytest_command.append("-v")

    if args.report:
        report_name = base.generate_timestamp() + "_report"
        pytest_command.append(f"--html=reports/{report_name}.html")

    if args.parallel:
        pytest_command.append("-n 4")

    subprocess.run(pytest_command)


if __name__ == "__main__":
    args = parse_args()
    run_tests(args)
