def bubblesort(elements):
    size = len(elements)
    
    for i in range(size-1):
        if elements[i] > elements[i+1]:
            tmp = elements[i]
            elements[i] = elements[i+1]
            elements[i+1] = tmp
            bubblesort(elements)

if __name__ == '__main__':
    elements = [5, 9, 2, 52, 42, 12, 54, 18 ,1]
    
    bubblesort(elements)
    print(elements)