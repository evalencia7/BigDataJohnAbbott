from mrjob.job import MRJob
from mrjob.step import MRStep

class MostRatedMovie(MRJob):

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
        max_views = -1
        max_movie_id = ""
        for kv in lst:
            if kv[0] > max_views:
                max_movie_id = kv[1]
                max_views = kv[0]
        yield (max_views, max_movie_id)
        
if __name__ == '__main__':
    MostRatedMovie.run()
