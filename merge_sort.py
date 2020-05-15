import random
import math
SIZE = 20

def merge_sort(random_list):
    if len(random_list)>1:
        middle = len(random_list)//2
        left_array = random_list[:middle]
        right_array = random_list[middle:]

        merge_sort(left_array)
        merge_sort(right_array)

        i=j=k=0

        while i<len(left_array) and j<len(right_array):
            if left_array[i]<=right_array[j]:
                random_list[k]=left_array[i]
                i+=1
            else:
                random_list[k]=right_array[j]
                j+=1
            k+=1
        
        while i<len(left_array):
            random_list[k]= left_array[i]
            i+=1
            k+=1
        while j<len(right_array):
            random_list[k]=right_array[j]
            j+=1
            k+=1



def merge_sort_alt(random_list,begin,end):
    if begin<end:
        middle = begin + (end-begin)//2

        merge_sort_alt(random_list,begin,middle)
        merge_sort_alt(random_list,middle+1,end)

        L=[]
        R=[]
        for i in range(begin,middle+1):
            L.append(random_list[i])
        for i in range(middle+1,end+1):
            R.append(random_list[i])

        L.append(math.inf)
        R.append(math.inf)
        i=j=0
        for k in range(begin,end+1):
            if L[i]<=R[j]:
                random_list[k]=L[i]
                i+=1
            else:
                random_list[k]=R[j]
                j+=1
            k+=1

if __name__ == '__main__':

    random_list = [random.randint(0,SIZE) for n in range(SIZE)]
    random_list2 = [random.randint(0,SIZE) for n in range(SIZE)]
    print('Random List 1: {}'.format(random_list))
    merge_sort(random_list)
    print('Sorted Random List 1: {}'.format(random_list))
    print('--------------------------------------------------------------------')
    print('Random List 2: {}'.format(random_list))
    merge_sort_alt(random_list2,0,SIZE-1)
    print('Sorted Random List 2: {}'.format(random_list))