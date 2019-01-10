def my_sort(lst):
  RADIX = 10
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
