import argparse
from teabreak.core import start_reminder


def main():
    parser = argparse.ArgumentParser(description="Take mindful tea breaks while you code.")
    parser.add_argument(
        "--every", "-e",
        type=int,
        default=60,
        help="Set break interval in minutes (default: 60)",
    )
    parser.add_argument(
        "--tea-mode", "-t",
        action="store_true",
        help="Enable Zen quotes and panda facts",
    )
    args = parser.parse_args()
    start_reminder(args.every, args.tea_mode)


if __name__ == "__main__":
    main()