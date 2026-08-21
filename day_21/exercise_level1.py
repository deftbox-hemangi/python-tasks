import statistics
from collections import Counter

class  Statistics():

    def __init__(self,data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)
    def mean(self):
        return sum(self.data) / len(self.data)
    def median(self):
        return statistics.median(self.data)
    def mode(self):
        return statistics.mode(self.data)
    def variance(self):
        return statistics.variance(self.data)
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def range(self):
        return self.max()-self.min()
    def std(self):
        return statistics.stdev(self.data)

    def freq_dist(self):
        frequency = Counter(self.data)

        return sorted([
            (count / self.count() * 100, value)
            for value, count in frequency.items()
        ], reverse=True)

    def describe(self):
        print(self.count())
        print(self.sum())
        print(self.mean())
        print(self.median())
        print(self.mode())
        print(self.variance())
        print(self.min())
        print(self.max())
        print(self.range())
        print(self.std())
        print(self.freq_dist())


ages=[31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data=Statistics(ages)
print(data.describe())

