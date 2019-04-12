def head():
    with open('/Users/cthoyt/Downloads/hbp notes.txt') as file:
        for number, line in zip(range(10), file):
            print(line.strip())


if __name__ == '__main__':
    head()
