def search_linear( example, list, result, searchnumber): 
    if result < list: 
        return -1
    if example[list] == searchnumber: 
        return list 
    if example[result] == searchnumber: 
        return result 
    return search_linear(example, list+1, result-1, searchnumber) 
  
example = [19, 2, 31, 45, 30, 11, 121, 27] 
number = len(example) 
searchnumber = 30
index = search_linear(example, 0, number-1, searchnumber) 
print("Het getal bevind zich op positie:")
print(index)
