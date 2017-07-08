from mrjob.job import MRJob
from mrjob.step import MRStep

class TotalByCustomerSorted(MRJob):

    def steps(self):
       return [
            MRStep(mapper=self.mapper_1,
                   reducer=self.reducer_1),
            MRStep(mapper=self.mapper_2,
                  reducer = self.reducer_2)
        ]
    def mapper_1(self, _, line):
        (customer, item, subtotal) = line.split(',')
        yield customer, float(subtotal)

    def reducer_1(self, customer, subtotal):
        yield sum(subtotal), customer

    def mapper_2(self, total, customer):
        yield total, customer

    def reducer_2(self, total, customer):
        yield total, list(customer)

if __name__ == '__main__':
    TotalByCustomerSorted.run()
