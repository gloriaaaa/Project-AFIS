import os
import operator
from collections import Counter
from itertools import groupby
from operator import itemgetter

#filepath="/home/gloria/NBIS_python-master/testfvc2002/fvc2002_testresult.txt"
filepath="/home/gloria/NBIS_python-master/testfingerprints/result-R2111000403002020050006.txt"
#filepath="/home/gloria/NBIS_python-master/testDB1_B/result_DB1-B.txt"
results=[]
with open(filepath, "r") as f:
    for line in f.readlines():
        result={}
        line = line.strip('\n')
        #print(line)
        score=line.split(" ")[0]
        #finger1=line.split(" ")[1].split("/")[-1].split(".")[0]
        #finger2=line.split(" ")[2].split("/")[-1].split(".")[0]
        finger1 = line.split(" ")[1].split("/")[-1].split(".")[0].split("_")[-1]
        finger2 = line.split(" ")[2].split("/")[-1].split(".")[0].split("_")[-1]
        result["score"]=int(score)
        result["finger1"] = finger1
        result["finger2"] = finger2
        #print(result)
        results.append(result)

result_list = sorted(results, key=operator.itemgetter('score'))

samepicture=[]
samefinger=[]
different=[]
for fingerprints in result_list:
    #if fingerprints["finger1"].split("_")[0]==fingerprints["finger2"].split("_")[0]:
    #    if fingerprints["finger1"].split("_")[1]==fingerprints["finger2"].split("_")[1]:
    #        samepicture.append(fingerprints)
    if fingerprints["finger1"].split("-")[0]==fingerprints["finger2"].split("-")[0]:
        if fingerprints["finger1"].split("-")[1]==fingerprints["finger2"].split("-")[1]:
            samepicture.append(fingerprints)
        else:
            samefinger.append(fingerprints)
    else:
        different.append(fingerprints)
print("samepicture",len(samepicture))
print("samefinger",len(samefinger))
print("different",len(different))
for threshold in range(0,31):
    #print("threshold score:",threshold)
    if len(result_list)!=len(samepicture)+len(samefinger)+len(different):
        print("error!")
    else:
        #print("samefinger result:")
        perhapswrong=0
        for data,items in groupby(samefinger,key=itemgetter('score')):
            list1=list(items)
            #print(data,len(list1),list1)
            if data<threshold:
                perhapswrong+=len(list1)
        #print("perhaps wrong percent:",perhapswrong,perhapswrong/len(samefinger))
        #print("different result:")
        perhapswrong1 = 0
        for data, items in groupby(different, key=itemgetter('score')):
            list1 = list(items)
            #print(data, len(list1),list1)
            if data>threshold:
                perhapswrong1+=len(list1)
        print(threshold, perhapswrong/len(samefinger), perhapswrong1 / len(different))
