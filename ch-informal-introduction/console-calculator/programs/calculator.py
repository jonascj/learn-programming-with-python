# Simple console calculator

def get_num(name):
    try: 
        n = float(input("{} = ".format(name)))
    except ValueError:
        print("Error: '{}' was not a number.".format(name))
        return

    return n

#print("######################")
print("## Console Calculator ##")
#print("######################")
print("")

print("  1: a + b")
print("  2: a - b")
print("  3: a * b")
print("  4: a / b")
print("  5: average of a_1, a_2 ... a_n")
print("  q: quit")
print("")


running = True
while running:

    op = input("Select operation: ")

    if op == "1":
        try: 
            a = float(input("  a = "))
        except ValueError:
            print("  Error: 'a' was not a number.")
            continue

        try: 
            b = float(input("  b = "))
        except ValueError:
            print("  Error: 'a' was not a number.")
            continue 

        c = a + b

        print("  {} + {} = {}".format(a,b,c))

    elif op == "2":
        print("2")
    elif op == "3":
        print("3")
    elif op == "4":
        a = get_num("  a")
        b = get_num("  b")
        if a and b:
            c = a / b
            print("  {} / {} = {}".format(a,b,c))

    elif op == "5":
        user_input = input("  Numbers to average (seperate by comma): ")
        
        numbers = []
        for u in user_input.split(","):
            try:
                n = float(u)
            except:
                print("  Error: '{}' is not a number".format(u))
                numbers = []
                break

            numbers.append(n)

        if len(numbers) > 0:
            s = 0
            for n in numbers:
                s = s + n

            avg = s/len(numbers)
        
            print("  Average: {}".format(s/len(numbers)))
            

        

    elif op == "q":
        running = False
    else:
        print("  Error: Unknown operation.")

    print()
    

