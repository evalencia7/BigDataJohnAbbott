from mrjob.job import MRJob

class NumOrdersFrequencyCount(MRJob):

    def mapper(self, _, line):
        (customer, item, subtotal) = line.split(',')
        fst = float(subtotal)
        if (fst <= 10.0):
            yield 0, subtotal
        if (fst > 10.0 and fst <= 20.0):
            yield 1, subtotal
        if (fst > 20.0):
            yield 2, subtotal
            
    def reducer(self, rango, subtotal):
        numOrders = 0
        for x in subtotal:
            numOrders += 1
        yield rango, numOrders

if __name__ == '__main__':
    NumOrdersFrequencyCount.run()
