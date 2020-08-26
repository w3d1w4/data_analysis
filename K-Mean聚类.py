from numpy import *

# dataSet = [[1, 2, 3, 2],
#            [2, 10, 4, 3],
#            [3, 3, 8, 5],
#            [2, 8, 5, 1],
#            [3, 3, 2, 9],
#            [3, 3, 10, 2]]

def loadDataSet():
    dataSet = []
    with open('Iris数据集', 'r') as f:
        #删除第一行
        f.readline()
        for line in f.readlines():
            curLine = line.strip().split(',')
            #删除最后的分类
            curLine.pop()
            #在Python3中要显示转换map的结果，map返回的是map类型
            fltLine = list(map(float, curLine))
            dataSet.append(fltLine)
    dataSet = mat(dataSet)
    return dataSet

dataSet = loadDataSet()

k = 4


# 计算欧式距离
def disEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


# 计算随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minJ)
        # 最小值加上范围*随机数作为质心
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


# K-Means函数
def kMeans(dataSet, k, distMeans=disEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = 1
            for j in range(k):
                distJI = distMeans(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
                    #如果计算的质心不等于现有质心，刚代表可以优化，设定clusterChanged=True
            if clusterAssment[i, 0] != minIndex: clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        #重新计算质心，通过把所有列的值取平均值来实现
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment

def biKmeans(dataSet, k, distMeans=disEclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    #第一次创建质心
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j, 1] = distMeans(mat(centroid0), dataSet[j, :])**2
    while (len(centList) < k):
        lowerestSSE = inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A == i)[0], :]
            centroidMat, splitClusterAss = kMeans(ptsInCurrCluster, 2, distMeans)
            sseSplit = sum(splitClusterAss[:, 1])
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])
            print("sseSplit, and notSplit:", sseSplit, sseNotSplit)
            if (sseSplit + sseNotSplit) < lowerestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClusterAss = splitClusterAss.copy()
                lowerestSSE = sseSplit + sseNotSplit
        bestClusterAss[nonzero(bestClusterAss[:, 0].A == 1)[0], 0] = len(centList)
        bestClusterAss[nonzero(bestClusterAss[:, 0].A == 0)[0], 0] = bestCentToSplit
        print("the bestCentToSplit is :", bestCentToSplit)
        print("the len of bestClusterAss is:", len(bestClusterAss))
        centList[bestCentToSplit] = bestNewCents[0, :]
        centList.append(bestNewCents[1, :])
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0], :] = bestClusterAss
        print(len(centList))
        print("----------------------------------------------------------------------")
    return centList, clusterAssment

biKmeans(dataSet, k )

