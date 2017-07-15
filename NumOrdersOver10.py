from mrjob.job import MRJob

class NumOrdersByAmountRange(MRJob):

    def mapper(self, _, line):
        (customer, item, subtotal) = line.split(',')
        fst = float(subtotal)
        yield fst // 10 * 10, subtotal

    def reducer(self, key, subtotal):
        numOrders = 0
        for x in subtotal:
            numOrders += 1
        yield int(key), numOrders

if __name__ == '__main__':
    NumOrdersByAmountRange.run()
