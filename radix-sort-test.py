def my_sort(lst):
  # Waarde "RADIX" aanpassen voor grotere getallen, hoe groter hoe langer het sorteren duurt.
  # Waarde RADIX = 10000 kan getallen tot 9999
  RADIX = 10000
  tmp , placement, = -1, 1,

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

    # Kijk of de lijst positief of negatief is en stop vervolgens de gesorteerde getallen in de juiste lijst
    for number in lst:
        if number > 0:
            return lstpositive
        else:
            return lstnegative

if __name__ == '__main__':
    lst = [210, -124, -7, 9324, 32, -10]
    print("Dit was de lijst voor de RADIX sortering:")
    print(lst)

    # Splits de lijst in 1 met positieve en 1 met negatieve cijfers
    lstpositive = []
    lstnegative = []
    for number in lst:
        if number > 0:
            lstpositive.append(number)
        else:
            lstnegative.append(number)

    # Sorteer beiden lijsten en voeg ze samen
    my_sort(lstpositive)
    my_sort(lstnegative)
    lst = lstnegative + lstpositive

    print("Dit was de lijst na de RADIX sortering:")
    print(lst)
