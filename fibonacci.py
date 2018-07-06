import sys

def fibonacci(n):
    if n == 1:
        sys.stdout.write('.')
        return 1
    elif n == 0:
        sys.stdout.write('.')
        return 0 
    else:
        sys.stdout.write('%d' % int(n-1))
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print(fibonacci(30))
