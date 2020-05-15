import random

SIZE = 20

def select_sort(random_list):
    for i in range(len(random_list)-1):
        idx_min = i
        for j in range(i+1,len(random_list)):
            if random_list[j]<random_list[idx_min]:
                idx_min = j

        random_list[i],random_list[idx_min] = random_list[idx_min],random_list[i]

if __name__ == '__main__':

    random_list = [random.randint(0,SIZE) for n in range(SIZE)]
    print('Random List: {}'.format(random_list))
    select_sort(random_list)
    print('Sorted Random List: {}'.format(random_list))