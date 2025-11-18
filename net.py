print("hello hey")
print("conflict avatte")
print("conflict veendum")
print("second line changed by hijas ca")
print("hijas aaane")
list = [1,2,4,[2,35,4,[2,34,3]]]
def re(list_):
    new = []
    for each_item in list_:
        if isinstance(list,list_):
            new.extend(re(each_item))
        else:
            new.append(each_item)


