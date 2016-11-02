# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            res = (i // 3**j) % 3
            if res == 1:
                bag1.append(items[j])
            elif res == 2:
                bag2.append(items[j])
        #yield (bag1, bag2)

powerSet([1,2])