from mrjob.job import MRJob
from mrjob.step import MRStep

class TwoMostRatedMovies(MRJob):

    def steps(self):
       return [
            MRStep(mapper=self.mapper_1,
                   reducer=self.reducer_1),
            MRStep(reducer=self.reducer_2)
        ]
    def mapper_1(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_1(self, movieID, occurences):
        yield None, (sum(occurences), movieID)
     
    def reducer_2(self, k, lst):
        newlst = list(lst)
        newlst.sort(reverse=True)
        for i in range(0, 10):       
            yield newlst[i]
       
if __name__ == '__main__':
    TwoMostRatedMovies.run()
