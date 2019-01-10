def search_linear(lst, item, index=0):
    if lst[0] == item:
        return index
    if len(lst[1:]) == 0:
        return False
    s = search_linear(lst[1:], item, index + 1)
    return s

example = [19, 2, 31, 45, 30, 11, 121, 27]
print("Het getal bevind zich op positie:")
print(search_linear(example, 30))
