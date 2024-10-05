import argparse

from src import file_operations

def main():
    parser = argparse.ArgumentParser(description='Simple version control system')
    parser.add_argument('command', help='Command to execute')
    parser.add_argument('args', nargs='*', help='Arguments for the command')

    args = parser.parse_args()
    print("arguments were: " , args)


if __name__ == "__main__":
    main()