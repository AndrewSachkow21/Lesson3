debats = [1,2,2,4,5,3,4,3,2,2,3,4,4,3,1,2,2,3,3,4,4,2,2,1,2,3,4,5,5,5,5,5,1,2,5,3,4,2,-1,32]
def debates(results):
    statistic = {"#1":0,"#2":0,"#3":0,"#4":0,"#5":0}
    percent = {"#1":0,"#2":0,"#3":0,"#4":0,"#5":0}
    final= ""
    for result in results:
        if result == 1:
            statistic["#1"]+=1
        elif result == 2:
            statistic["#2"]+=1
        elif result == 3:
            statistic["#3"]+=1
        elif result == 4:
            statistic["#4"]+=1
        elif result == 5:
            statistic["#5"]+=1
    for i in range(1,len(percent)+1):
        percent["#"+str(i)] = statistic["#"+str(i)]*100/len(results)
    sorted_list = list(dict(sorted(percent.items(), key=lambda item: item[1])))
    for i in range(len(sorted_list),0,-1):
        print(sorted_list[i-1], "|",  percent[sorted_list[i-1]],"%|", statistic[sorted_list[i-1]])
 

print(debates(debats))
