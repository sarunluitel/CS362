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

data = [x for x in range(0, 100)]

random.shuffle(data)


def quickSelect(data, k):
    if len(data) == 1: return data[0]

    pivot = random.choice(data)

    sSet, lSet = [], []

    for x in data:
        if x <= pivot: sSet.append(x)
        if x > pivot: lSet.append(x)

    if len(sSet) >= k:
        return quickSelect(sSet, k)
    elif len(sSet) < k:
        return quickSelect(lSet, k - len(sSet))


print(quickSelect(data, 62))
