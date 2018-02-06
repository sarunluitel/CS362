# Implement the QuickSearch and Median-of-Medians algorithms discussed in class.  Add suitable code to keep track of how
# many comparisons are done between pairs of array elements.  Then, test your code as follows:
# Generate a randomly ordered array, A, of 100 distinct elements.  Run both of the QS and MoM algorithms on it to find
# the 50th smallest element.  Specifically, run QS 100 times on array A, and store the comparison count for each run.
# Run MoM on array A once (or twice, to make sure the count is the same both times) and store its comparison count.
# Repeat the above experiment 100 times, storing all the comparison counts data.
# Next, use this data to compute the following quantities:
#
# 1. Find the overall average number of comparisons needed by each algorithm.
# 2. Determine in how many of the 10,000 trials of QS was the number of comparisons more than the number needed by MoM
#  on the same input.
# 3. For the 100 runs of MoM, find the minimum, 10th percentile, median, 90th percentile, and maximum number of comparisons done.
# 4. Do the same for the 10K runs of QS.
# Submit your code and its output on Learn.
# There are some associated online questions that you will also need to answer.  This Survey is available just below,
# and is a required part of the assignment.

import random
import numpy as np


class C(object):
    MoMCompare = 0


def quickSelect(dataQs, k, QsCompare):
    if len(dataQs) == 1: return dataQs[0], QsCompare

    pivot = random.choice(dataQs)

    sSet, lSet = [], []

    for x in dataQs:
        QsCompare += 1
        if x < pivot: sSet.append(x)
        if x >= pivot: lSet.append(x)

    if len(sSet) >= k:
        return quickSelect(sSet, k, QsCompare)
    elif len(sSet) < k:
        return quickSelect(lSet, k - len(sSet), QsCompare)


def MoM(dataMoM, i):
    sublists = [dataMoM[j:j + 5] for j in range(0, len(dataMoM), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]  # get the pivot
    else:
        pivot = MoM(medians, len(medians) // 2)  # recursion to create smallar chunks

    sSet, lSet = [], []

    for x in dataMoM:
        C.MoMCompare += 1
        if x < pivot: sSet.append(x)
        if x > pivot: lSet.append(x)

    k = len(sSet)
    if i < k:
        return MoM(sSet, i)
    elif i > k:
        return MoM(lSet, i - k - 1)
    else:
        return pivot


data = [x for x in range(0, 100)]
totalQS = []
totalMoM = []
QSmoreThenMom = 0

for i in range(0, 100):
    random.shuffle(data)
    for j in range(0, 100):
        QS = quickSelect(data, 50, 0)[1]
        C.MoMCompare = 0
        MoM(data, 50)
        MOM = C.MoMCompare
        if QS > MOM: QSmoreThenMom += 1

        totalQS.append(QS)

    totalMoM.append(C.MoMCompare)

a = np.array(totalMoM)
b = np.array(totalQS)

print('Q1. Average comparasion in QS is  ' + str(sum(totalMoM) / len(totalMoM)))
print('Q2. QS did ' + str(QSmoreThenMom) + ' times more comparision more than MoM')
print('Q3. descriptive Statistics')

print('MoM Comparasions statistics: Minimum ' + str(min(totalMoM)))
print('         10th percentile = ' + str(np.percentile(a, 10)))
print('         Median = ' + str(np.percentile(a, 50)))
print('         90th percentile = ' + str(np.percentile(a, 90)))
print('         Max = ' + str(max(totalMoM))+'\n')

print('QS Comparasions statistics: Minimum ' + str(min(totalQS)))
print('         10th percentile = ' + str(np.percentile(b, 10)))
print('         Median = ' + str(np.percentile(b, 50)))
print('         90th percentile ' + str(np.percentile(b, 90)))
print('         Max = ' + str(max(totalQS)))

