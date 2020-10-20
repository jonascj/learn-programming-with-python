# A simple calculator made as an introduction to programming

while True:
    print("Calculate a + b:")
    in1 = input("a=")
    in2 = input("b=")

    if in1 == "quit":
        break

    try:
        a = int(in1)
        b = int(in2)
    except ValueError: 
        print("Error: a or b was an invalid number")
        continue

    c = a+b
    output = "{}+{}={}".format(a,b,c)
    print(output)
