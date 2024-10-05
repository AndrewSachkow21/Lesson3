debats = [1,2,2,4,5,3,4,3,2,2,3,4,4,3,1,2,2,3,3,4,4,2,2,1,2,3,4,5,5,5,5,5,1,2,5,3,4,2,-1,32]
def debates(results):
    statistic = {"#1":0,"#2":0,"#3":0,"#4":0,"#5":0}
    result2=100/len(debats)
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
    print(statistic)
print(debates(debats))