import sys

def reducer():
    max_length = 0
    longest_paths = []

    for line in sys.stdin:
        path_length, path = line.strip().split("\t", 1)
        path_length = int(path_length)

        if path_length > max_length:
            max_length = path_length
            longest_paths = [path] 
        elif path_length == max_length:
            longest_paths.append(path)  

    for path in longest_paths:
        print(f"{max_length}\t{path}")

if __name__ == "__main__":
    reducer()
