while True:
    a = input()
    b = input()
    true1 = 0
    true2 = 0
    true3 = 0
    true4 = 0
    for i in range (len(a)):
        if "0" <= a[i] <= "9":
            print("Wrong answer")
            break
        else:
            if "a" <= a[i] <= "z" or "A" <= a[i] <= "Z":
                true1 = true1 + 1
            elif "�" <= a[i] <= "�" or "�" <= a[i] <= "�":
                true2 = true2 + 1
    for i in range (len(b)):
        if "0" <= b[i] <= "9":
            print("Wrong answer")
            break
        else:
            if "a" <= b[i] <= "z" or "A" <= b[i] <= "Z":
                true3 = true3 + 1
            elif "�" <= b[i] <= "�" or "�" <= b[i] <= "�":
                true4 = true4 + 1
    if true1 == len(a) and true4 == len(b):
        print("������� ����� -", b)
        print("The English word is", a)
    elif true2 == len(a) and true3 == len(b):
        print("������� ����� -", a)
        print("The English word is", b)
    else:
        print("Wrong answer")
    break
