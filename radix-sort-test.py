def my_sort(lst):
  # Waarde "RADIX" aanpassen voor grotere getallen, hoe groter hoe langer het sorteren duurt.
  # Waarde RADIX = 10000 kan getallen tot 9999
  RADIX = 10000
  tmp , placement = -1, 1

  while True:
    buckets = [list() for _ in range( RADIX )]

    for i in lst:
      tmp = int((i / placement) % RADIX)
      buckets[tmp].append(i)

    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        lst[a] = i
        a += 1

    placement *= RADIX
    return lst

if __name__ == '__main__':
    lst = [210, 7, 124, 9324, 32, 10]
    print("Dit was de lijst voor de RADIX sortering:")
    print(lst)
    my_sort(lst)
    print("Dit was de lijst na de RADIX sortering:")
    print(lst)
