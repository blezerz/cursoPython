serie = "N-02"

if serie =="N-01":
    print("samsung")
elif serie =="N-02":
    print("samsung")
elif serie =="N-03":
    print("samsung")
else:
    print("no existe ese producto")

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case"N-03":
        print("motorola")
    case _:
        print("no existe")