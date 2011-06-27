import nltk
import numpy

def demo():
    # example from figure 14.9, page 517, Manning and Schutze

    from nltk import cluster

    vectors = [numpy.array(f) for f in [[2, 1], [1, 3], [4, 7], [6, 7]]]
    means = [[4, 3], [5, 5]]

    clusterer = cluster.KMeansClusterer(2, cluster.util.euclidean_distance, initial_means=means)
    clusters = clusterer.cluster(vectors, True, trace=True)

    print 'Clustered:', vectors
    print 'As:', clusters
    print 'Means:', clusterer.means()
    print

    vectors = [numpy.array(f) for f in [[3, 3], [1, 2], [4, 2], [4, 0], [2, 3], [3, 1]]]
    
    # test k-means using the euclidean distance metric, 2 means and repeat
    # clustering 10 times with random seeds

    clusterer = cluster.KMeansClusterer(2, cluster.util.euclidean_distance, repeats=10)
    clusters = clusterer.cluster(vectors, True)
    print 'Clustered:', vectors
    print 'As:', clusters
    print 'Means:', clusterer.means()
    print

    # classify a new vector
    vector = numpy.array([3, 3])
    print 'classify(%s):' % vector,
    print clusterer.classify(vector)
    print

if __name__ == '__main__':
    demo()

