# A simple calculator made as an introduction to programming

while True:
    print("Calculate a + b:")
    in1 = input("a=")
    in2 = input("b=")

    if in1 == "quit":
        break

    a = int(in1)
    b = int(in2)
    c = a+b
    output = "{}+{}={}".format(a,b,c)
    print(output)
