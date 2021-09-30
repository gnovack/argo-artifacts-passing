import random


def main():
    random_number = random.randint(1, 10)
    with open('/tmp/output', 'w') as out_file:
        out_file.write(str(random_number))

if __name__ == '__main__':
    main()
