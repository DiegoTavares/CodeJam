#!/usr/bin/env python

import sys


#n_items = 100
#credit = 542; # 5..1000
#items = [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789]

def selectItems(num_case, n_item, credit, items):
    items.sort()
    #print(items)
    found = False

    counter = 0
    l = 0
    r = n_items - 1
    l_up = True

    while items[r] > credit :
        r = r - 1
    while not found and l < r :
        while items[l] + items[r] < credit :
            l = l + 1
            counter = counter + 1

        if items[l] + items[r] == credit :
            found = True
        else : # = or >
            r = r - 1
            l = 0
        counter = counter + 1
    if found:
        sorted(items)
    	print("Case #%d = %d %d" %(num_case, items[l], items[r]))
    else:
    	print("Not found")
    print(counter)

if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as f:
        num_tests = int(f.readline())
        for i in range(num_tests):
            credit = int(f.readline())
            n_items = int(f.readline())
            items = [int(x) for x in f.readline().split(' ')]
            selectItems(i+1, n_items, credit, items)
