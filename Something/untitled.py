def diamond1(w):
    for i in list(range(w)) + list(range(w - 2, -1, -1)):
        print(" " * (w - 1 - i) + "*" * (i * 2 + 1))

diamond1(5)
# first list = [0,1,2,3,4]
# second list = [3,2,1,0]

#%%
def decorFunc(oriFunc):
    def wrapperFunc():
        print("Mampus lu")
        return oriFunc()

    return wrapperFunc


@decorFunc
def display():
    print("Woah")
# %%
