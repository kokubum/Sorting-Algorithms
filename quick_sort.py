import random

SIZE = 20

def partition(random_list,begin,end):
    idx = begin-1
    pivot = random_list[end]

    for j in range(begin,end):
        if random_list[j]<=pivot:
            idx+=1
            random_list[idx],random_list[j] = random_list[j],random_list[idx]
    random_list[idx+1],random_list[end] = random_list[end],random_list[idx+1]


    return (idx+1)
        
def quick_sort(random_list,begin,end):
    if begin<end:

        pivot = partition(random_list,begin,end)

        quick_sort(random_list,begin,pivot-1)
        quick_sort(random_list,pivot+1,end)

if __name__ == '__main__':

    random_list = [random.randint(0,SIZE) for n in range(SIZE)]
    random_list2 = [random.randint(0,SIZE) for n in range(SIZE)]
    print('Random List: {}'.format(random_list))
    quick_sort(random_list,0,SIZE-1)
    print('Sorted Random List: {}'.format(random_list))

