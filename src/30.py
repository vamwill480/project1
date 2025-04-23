import os
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--debug":
        print("Debug mode is enabled")
        # Add your debug code here
    else:
        print("Project1 code generated")

if __name__ == "__main__":
    main()
