import collections
def main():
    a = {'name': 'Carl', 'age': 23}
    b = {'pet': 'Dog', 'age': 3}

    cm = collections.ChainMap(a,b)
    print(cm['age'])
    a['age'] = 33;
    print(cm['age'])

    for k,v in cm.items():
        print(k,'->',v)

    #We can see that both values for age is stored in cm
    print(cm)
    #It is stored in a list called maps
    print(cm.maps)

    #What happens if we reorder it?
    cm.maps = list(reversed(cm.maps))
    for k, v in cm.items():
        print(k, '->', v) #We get the dogs age!

    #We can spawn children from the chain map
    cm_child = cm.new_child()
    print('Printing cm_child')
    for k,v in cm_child.items():
        print(k,'->',v)
    #What happens if we change something for cm_child?
    cm_child['age'] = 9
    print(cm)
    print(cm_child)

if __name__ == '__main__':
    main()