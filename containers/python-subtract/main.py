import sys

def main():
    value_1, value_2 = int(sys.argv[1]), int(sys.argv[2])
    with open('/tmp/output', 'w') as out_file:
        out_file.write(str(value_1 - value_2))

if __name__ == "__main__":
    main()
