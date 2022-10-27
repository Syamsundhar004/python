if 0:
    minimum = int(input(" Please Enter the Minimum Value : "))
    maximum = int(input(" Please Enter the Maximum Value : "))
    while minimum <= maximum:
        if(minimum % 2 == 0):
            print(minimum)
        minimum = minimum + 1
if 0:
    list1=[5,7,3,9,1]
    list2=[6,8,2,4,10]
    list3=list1+list2
    print(list3)
    list3.sort(reverse=True)
    print(list3)
    #a=list3[::-1]
    #print(a)
    print(dir(list3))
    print(help(list3.sort))
if 0:
    dict1={"apple":1,"orange":2,"guava":3}
    dict1.update({"banana": "10"})
    dict1["berry"]= 20
    print(dict1)
if 0:
    list4=('jjj','b','c','d','e')
    for var in list4:
        if var.startswith('a'):
            print("Vowels :",var)
        else:
            print("Constanents :",var)
if 0:
    dict2={1:"abac", 2:"acbc",3:"dada"}
    for key,value in dict2.items():
        if value.startswith("a"):
            print(value)
            print(value.count('a'))
if 0:
    list5=[123,321,1,2,3,3,2,1,4,5,3,2,3,4]
    count = {}
    for i in list5:
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1

    print(count)
list6=[1,2,3,4,5,6,7,8,9,10]
