def fibo(n):
    if n<2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

if __name__=="__main__":
    print(fibo(4))

