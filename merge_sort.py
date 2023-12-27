def merge(first,second):
    mix = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            mix.append(first[i])
            i += 1
        else:
            mix.append(second[j])
            j += 1
    mix += first[i:]
    mix += second[j:]
    return mix

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

if __name__ == '__main__':
    arr = [-12,-2,15,22,-1,3,4,2,6,7,0,8]
    print(mergeSort(arr))
    

  


