#!/usr/bin/env python
""" Checks if new code creates signfificantly different results with old code.
Note, that significant difference might be desirable --- this test allows to
find out which changes exactly happened."""
import math
import sys
import time
import difflib
import pickle
from netineti.trainer import NetiNetiTrainer
from netineti.finder import NetiNeti

num_cycles = 3

if len(sys.argv) > 1:
    try:
        num_cycles = int(sys.argv[1]) + 1
    except ValueError:
        pass

def mean(population):
    ave = 0.0
    n=0
    for x in population:
        n = n + 1
        ave = ave + x

    return ave / n

def variance(population):
    n = 0
    mean = 0.0
    s = 0.0
    for x in population:
        n = n + 1
        delta = x - mean
        mean = mean + (delta / n)
        s = s + delta * (x - mean)

    return s / (n-1)

# calculate the standard deviation of a population
# accepts: an array, the population
# returns: the standard deviation
def standard_deviation(population):
    if len(population) == 1:
        return 0
    return math.sqrt(variance(population))


population = []

time_start = time.clock()
classifier = NetiNetiTrainer(learning_algorithm='NB')
pickle.dump(classifier, open('../data/netineti_trainer_dump', 'wb'))
time_training = time.clock()
print "Training time: %s" % (time_training - time_start)
nn = NetiNeti(classifier)
for i in range(1, num_cycles):
    print "going through the cycle %s" % i
    time_start = time.clock()
    result = nn.find_names(open("../data/test.txt").read())
    print "Name finding time: %s" % (time.clock() - time_start)

    test_result_file = open("../data/test_result_after_refactoring.txt", 'w')

    for i in result[1]:
        test_result_file.write(i + "\n")

    test_result_file.close()

    test_result_before_refactoring = open('../data/test_result_before_refactoring.txt').read().splitlines()
    test_result_after_refactoring = open('../data/test_result_after_refactoring.txt').read().splitlines()

    d = difflib.Differ()
    delta = d.compare(test_result_after_refactoring, test_result_before_refactoring)

    ins = []
    outs = []
    for i in delta:
        if len(i) > 0:
            if i[0] == '+': #insert
                outs.append(i.strip())
            if i[0] == '-': #delete
                ins.append(i.strip())
        differences = ins + outs

    #recall = TP / N_before
    recall = (len(test_result_before_refactoring) - len(outs)) * 1.0/len(test_result_before_refactoring)

    #precision = TP/N_after
    precision = (len(test_result_before_refactoring) - len(outs)) * 1.0/len(test_result_after_refactoring)

    f1_score = 2*recall * precision / (recall + precision)

    population.append([recall, precision, f1_score])

#get the average precision, recall and f-measure

recalls = [p[0] for p in population]
precisions = [p[1] for p in population]
f1_scores = [p[2] for p in population]

print '', '\t', 'recall', '\t', 'precision', '\t', 'f1_score'
print 'Mean', '\t', mean(recalls), '\t', mean(precisions), '\t', mean(f1_scores)
print differences
