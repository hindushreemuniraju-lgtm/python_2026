marks=float(input("enter the marks"))


if marks>=35:         # in the loop if we use another loop it is called as nested loop
    print("pass")

    if marks>=90:
        print("medical field")

    elif marks>=75:
        print("engineering field")

    elif marks>=60:
        print("law field")

    else:
        print("degree field")


else:
    print("FAIL.. BRO!!! DO BUSINESS AND GIVE JOBS FOR THE PASSED STUDENTS")

