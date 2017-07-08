from mrjob.job import MRJob

class TotalByCustomer(MRJob):

    def mapper(self, _, line):
        (customer, item, subtotal) = line.split(',')
        yield customer, float(subtotal)
    
    def reducer(self, customer, subtotal):
        yield customer, sum(subtotal)

if __name__ == '__main__':
    TotalByCustomer.run()
