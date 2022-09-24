def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

@dec1
def testing():
    print("learning decorator")

testing()