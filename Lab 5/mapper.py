import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()  
        path_length = len(line)
        print(f"{path_length}\t{line}") 

if __name__ == "__main__":
    print("running....")
    mapper()
