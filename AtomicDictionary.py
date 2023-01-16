def AtomicDictionary():
    ele={"na":"sodium","he":"helium"}
    print(ele)
    unikey=input("enter the uniq symbol")
    unisub=input("ente the name for the symbol {}".format(unikey))
    ele.update({unikey:unisub})
    print(ele)

    unikey=input("enter the duplicate symbol")
    unisub=input("ente the name for the symbol {}".format(unikey))
    ele.update({unikey:unisub})
    print(ele)


    print("total no of elements is {}".format(len(ele)))
    s=input("enter the element to be searched")
    if s in ele.values():
        print("element found")
    else:
        print("not found")

