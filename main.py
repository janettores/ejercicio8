from Conjunto import conjunto
if __name__=='__main__':
    conjunto1= conjunto([1,2,3,4])
    conjunto2= conjunto([3,6,9])
    op=int(input("\n1- A + B\n2- A - B\n3- A = B\nIngrese una opcion (0 Para terminar): "))
    while op != 0:
        print("A: {}".format(conjunto1))
        print("B: {}".format(conjunto2))
        if op == 1:
            print("A+B= {}".format(conjunto1 + conjunto2))
        elif op == 2:
            print("A-B = {}".format(conjunto1 - conjunto2))
        elif op == 3:
            print("A=B : {}".format(conjunto1 == conjunto2))
        op = int(input("\n1- A + B\n2- A-B\n3-A=B\nIngrese una opcion (0 Para terminar): "))
    print("--FIN--")