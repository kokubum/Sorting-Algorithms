import random

SIZE = 20


def bubble_sort(random_list):
    for i in range(len(random_list)):
        for j in range(len(random_list)-1):
            if random_list[j]>random_list[j+1]:
                random_list[j],random_list[j+1]=random_list[j+1],random_list[j]


def bubble_sort_alt(random_list):
    swap = True
    while swap:
        swap = False
        for j in range(len(random_list)-1):
            if random_list[j]>random_list[j+1]:
                random_list[j],random_list[j+1]=random_list[j+1],random_list[j]
                swap = True

if __name__ == '__main__':

    random_list = [random.randint(0,SIZE) for n in range(SIZE)]
    random_list2 = [random.randint(0,SIZE) for n in range(SIZE)]
    print('Random List 1: {}'.format(random_list))
    bubble_sort(random_list)
    print('Sorted Random List 1: {}'.format(random_list))
    print('--------------------------------------------------------------------')
    print('Random List 2: {}'.format(random_list))
    bubble_sort_alt(random_list2)
    print('Sorted Random List 2: {}'.format(random_list))