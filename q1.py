def cond(a,b,c):
    if (-b/a > 0 and c/a > 0):
        return "tem raiz real"

    return "nao tem raiz real"

print(cond(1,2,1))