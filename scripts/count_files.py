import os

def count_files():
    file_count = sum(len(files) for _, _, files in os.walk('.'))
    print(f"Total files in repo: {file_count}")

if __name__ == "__main__":
    count_files()
