train=[{1:None,2:None,3:None,4:None},{5:None,6:"ч",7:"ч",8:None},{9:"ч",10:"ж",11:None,12:"ж"},{13:None,14:None,15:None,16:"ж"},{17:None,18:None,19:None,20:None,},{21:None,22:"Ч",23:"ч",24:"ч"},{25:"ж",26:None,27:"ж",28:None}]
def empty_compartment_list(train):
    empty_compartment_list = []
    compartment_number = 0
    cuounter = 0
    empty_value = 0
    for compartment in train:
        compartment_number += 1
        for i in range(4):            
            cuounter += 1
            if compartment[cuounter] == None:
                empty_value += 1
            else:
                empty_value = 0
        if empty_value == 4:
            empty_compartment_list.append(("купе під номером",compartment_number,"ніким не зайняте"))
    return empty_compartment_list
def empty_places_list(train):
    empty_place_list = []
    counter = 0
    for compartment in train:
        for place in range(4):
            counter += 1
            if compartment[counter] == None:
                empty_place_list.append(counter)
    return empty_place_list
def empty_top_or_down_places(train,mode):
    counter = 0
    empty_top_place_list = []
    empty_down_place_list = []
    for compartment in train:
        for i in range(4):
            counter += 1
            if counter%2 == 0 and compartment[counter] == None:
                empty_top_place_list.append(counter)
            elif compartment[counter] == None and not counter%2 == 0:
                print(counter)
                empty_down_place_list.append(counter)
    if mode == 1:
        return empty_down_place_list
    else:
        return empty_top_place_list
def men_or_women_compartments(train,mode):
    counter = 0
    women_compartment_list = []
    men_compartment_list= []
    answer = [men_compartment_list,women_compartment_list]
    men = 0
    women = 0
    compartment_number = 0 
    
    for compartment in train:
        compartment_number += 1
        for i in range(4):
            counter += 1
            if compartment[counter] == "ч":
                men = True
            elif compartment[counter] == "ж":
                women = True
        if women == True and men == False:
            women_compartment_list.append(compartment_number)
        elif women == False and men == True:
            men_compartment_list.append(compartment_number)
        women = False
        men = False
    return answer[mode]
print(men_or_women_compartments(train,0))
