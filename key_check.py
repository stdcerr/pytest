dat={'row_1':123,'row_2':456,'row_3':789}

for i in range(1,10):
    print(i)
    key = "row_"+str(i)
    print(key)
    if key in dat:
        print(dat[key])
