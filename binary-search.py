def search_binary(lst, item):
    def recurse(first, last):
        mid = int((first + last) / 2)
        if first > last:
            return None
        elif lst[mid] < item:
            return recurse(mid + 1, last)
        elif lst[mid] > item:
            return recurse(first, mid - 1)
        else:
            return mid

    return recurse(0, len(lst) - 1)

example = [2, 11, 19, 27, 30, 31, 45, 121]
print("Het getal bevind zich op positie:")
print(search_binary(example, 31))
