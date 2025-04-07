import sys
with open(sys.argv[1], 'rb') as f:
        data = f.read()
        with open(sys.argv[2], 'w') as f:
                f.write(str(len(data)) + '\n')
