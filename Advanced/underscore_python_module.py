class Underscore(object):
    def map(self, arr, func):
        result = []
        for i in arr:
            result.append(func(i))
        return result

    def reduce(self, arr, func, memo):
        for i in arr:
            memo = func(i, memo)
        return memo

    def find(self, arr, func):
        for i in arr:
            if func(i):
                return i
        return "undefined"

    def filter(self, arr, func):
        result = []
        for i in arr:
            if func(i):
                result.append(i)
        return result
    def reject(self, arr, func):
        result = []
        for i in arr:
            if not func(i):
                result.append(i)
        return result

_ = Underscore()

evens = _.filter([1,2,3], lambda x: x % 2 == 0)
print evens

finds = _.find([1,2,3], lambda x: x == 2)
print finds

mappings = _.map([1,2,3], lambda x: x*3)
print mappings

reducing = _.reduce([1,2,3], (lambda x, y: x+y), 0)
print reducing

rejecting = _.reject([1,2,3], lambda x: x % 2 == 0)
print rejecting
