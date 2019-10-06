import math; #For pow and sqrt
import sys;
from random import uniform;
import matplotlib.pyplot as plt;

# IMPORTANT THINGS TO NOTE:
# mean and item are both arrays of [x, y]

###_Pre-Processing_###
def ReadData(fileName):
    #Read the file, splitting by lines
    f = open(fileName,'r');
    lines = f.read().splitlines();
    f.close();

    items = [];

    for i in range(len(lines)):
        line = lines[i].split('q');
        itemFeatures = [];

        # Checks the x and y that it just scraped and,
        # if it's within range, add it to the items[][] array.
        for j in range(len(line)):
            if j == 0:
                v = float(line[j]); # Convert feature value to float
                if (v >= 35.75 and v <= 36.1):
                    itemFeatures.append(v);
            if j == 1:
                v = float(line[j]); # Convert feature value to float
                if (v >= -79.2 and v <= -78.85):
                    itemFeatures.append(v);

        # This is just checking to make sure that the
        # array we're adding to array[] is full
        # This mf took ages to debug stg
        if (len(itemFeatures) == 2):
            items.append(itemFeatures);
    return items;

def FindColMinMax(items):
    n = len(items[0]);
    minima = [sys.maxsize for i in range(n)];
    maxima = [-sys.maxsize -1 for i in range(n)];

    for item in items:
        for f in range(len(item)):
            if(item[f] < minima[f]):
                minima[f] = item[f];

            if(item[f] > maxima[f]):
                maxima[f] = item[f];

    return minima,maxima;

def EuclideanDistance(x,y):
    S = 0; #The sum of the squared differences of the elements
    for i in range(len(x)):
        S += math.pow(x[i]-y[i],2);

    return math.sqrt(S); #The square root of the sum

def InitializeMeans(items,k,cMin,cMax):
    #Initialize means to random numbers between
    #the min and max of each column/feature

    f = len(items[0]); #number of features
    means = [[0 for i in range(f)] for j in range(k)];

    for mean in means:
        mean[0] = uniform(35.5, 36.5);
        mean[1] = uniform(-79.5, -78.5);

    return means;

def UpdateMeanAdd(n,mean,item):
    for i in range(1):
        m = mean[i];
        m = (m*(n-1)+item[i])/float(n);
        mean[i] = m;

    return mean;

def UpdateMean(n,mean):
    for i in range(len(mean)):
        m = mean[i];
        m = (m*(n))/float(n);
        mean[i] = m;

    return mean;

def FindClusters(means,items):
    clusters = [[] for i in range(len(means))]; #Init clusters

    for item in items:
        #Classify item into a cluster
        index = Classify(means,item);

        #Add item to cluster
        clusters[index].append(item);

    return clusters;


###_Core Functions_###
def Classify(means,item):
    #Classify item to the mean with minimum distance

    minimum = sys.maxsize;
    index = -1;

    for i in range(len(means)):
        #Find distance from item to mean
        dis = EuclideanDistance(item,means[i]);

        if(dis < minimum):
            minimum = dis;
            index = i;

    return index;

def CalculateMeans(k,items,maxIterations=100000):
    #Find the minima and maxima for columns
    cMin, cMax = FindColMinMax(items);

    #Initialize means at random points
    means = InitializeMeans(items,k,cMin,cMax);

    #Initialize clusters, the array to hold
    #the number of items in a class
    clusterSizes = [0 for i in range(len(means))];

    #An array to hold the cluster an item is in
    belongsTo = [0 for i in range(len(items))];

    #Calculate means
    for e in range(maxIterations):
        #If no change of cluster occurs, halt
        noChange = True;
        for i in range(len(items)):
            item = items[i];
            #Classify item into a cluster and update the
            #corresponding means.

            index = Classify(means,item);

            clusterSizes[index] += 1;
            means[index] = UpdateMeanAdd(clusterSizes[index],means[index],item);


            #Item changed cluster
            if(index != belongsTo[i]):
                noChange = False;

            belongsTo[i] = index;

        for i in range(len(means)):
            UpdateMean(clusterSizes[index], means[index])

        #Nothing changed, return
        if(noChange):
            break;

    return means;

def plotData(items, clusters):
    xVals1 = [];
    yVals1 = [];
    xVals2 = [];
    yVals2 = [];
    xVals3 = [];
    yVals3 = [];
    xVals4 = [];
    yVals4 = [];
    for i in range(len(clusters[0])):
        xVals1.append(clusters[0][i][1]);
        yVals1.append(clusters[0][i][0]);
    for i in range(len(clusters[1])):
        xVals2.append(clusters[1][i][1]);
        yVals2.append(clusters[1][i][0]);
    for i in range(len(clusters[2])):
        xVals3.append(clusters[2][i][1]);
        yVals3.append(clusters[2][i][0]);
    for i in range(len(clusters[3])):
        xVals4.append(clusters[3][i][1]);
        yVals4.append(clusters[3][i][0]);
    plt.plot(xVals1, yVals1, 'ro', xVals2, yVals2, 'bo', xVals3, yVals3, 'go', xVals4, yVals4, 'co');
    plt.show()
#    print(xVals2);
#    print(xVals6);
    

def main():

    # k is the number of clusters, you can mess around
    # with it if more/less than 6 gives better results
    k = 4;
    items = ReadData('yes.txt');
    means = CalculateMeans(k,items);
    clusters = FindClusters(means,items);
    # The output of this program is below, so
    # all you'll see is an array of the locations of the means
    print(means);
    plotData(items, clusters);
    # If you want to see all the points, uncomment the
    #line below
    #print(clusters);
    # This will print an array of arrays of all the points,
    # but they're organized by cluster

if __name__ == "__main__":
    main();
