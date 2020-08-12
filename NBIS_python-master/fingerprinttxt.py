filepath="/home/gloria/NBIS_python-master/testfingerprints/result-R2111000403002020050006.txt"
newfilepath="/home/gloria/NBIS_python-master/testfingerprints/result-R2111000403002020050006.txt"
results=[]
with open(filepath, "r") as f:
    for line in f.readlines():
        result={}
        line = line.strip('\n')
        #print(line)
        score=line.split(" ")[0]
        finger1=line.split(" ")[1].split("/")[-1].split(".")[0]
        finger2=line.split(" ")[2].split("/")[-1].split(".")[0]
        result["score"]=int(score)
        result["finger1"] = finger1
        result["finger2"] = finger2
        #print(result)
        results.append(result)
