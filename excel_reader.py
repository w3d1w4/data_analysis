from functools import reduce

import pandas as pd

data_frame = pd.read_excel("ps.xlsx")

def loadDataSetPSE():
    #选取一列
    provinceSet = set(data_frame["PSE省份"])
    m = data_frame.shape[0]
    provinceList = list(provinceSet)
    count = [0]*len(provinceList)
    for i in range(m):
        province = data_frame.loc[i, "PSE省份"]
        if  province in provinceList:
            index =provinceList.index(province)
            count[index] +=1
    return provinceList,count


def loadDataSetProject():
    #选取一列
    provinceSet = set(data_frame["项目省份"])
    m = data_frame.shape[0]
    provinceList = list(provinceSet)
    count = [0]*len(provinceList)
    for i in range(m):
        province = data_frame.loc[i, "项目省份"]
        if  province in provinceList:
            index =provinceList.index(province)
            count[index] +=1
    return provinceList,count

def loadDataSetEngineerScore():
    #选取一列
    engineerSet = set(data_frame["工程师姓名"])
    m = data_frame.shape[0]
    engineerList = list(engineerSet)
    count = [0]*len(engineerList)
    score = [0]*len(engineerList)
    for i in range(m):
        province = data_frame.loc[i, "工程师姓名"]
        if  province in engineerList:
            index =engineerList.index(province)
            count[index] += 1
            score[index] += data_frame.loc[i, "分数"]
    meanScore = list(map(lambda x,y: x/y, score, count ))
    engineerList.pop(0)
    count.pop(0)
    meanScore.pop(0)
    return engineerList,count, meanScore

