def my_sort(lst):
  # Waarde "RADIX" aanpassen voor grotere getallen, hoe groter hoe langer het sorteren duurt.
  # Waarde RADIX = 10000 kan getallen tot 9999
  RADIX = 10000
  tmp , placement, = -1, 1,
  
  # Splits de lijst in 1 met positieve en 1 met negatieve cijfers
  lstpositive = []
  lstnegative = []
  for number in lst: 
    if number > 0: 
        lstpositive.append(number)
    else: 
        lstnegative.append(number)
  
  print ("Tussentijdse splitsing:")      
  print (lstpositive)
  print (lstnegative)

  while True:
    buckets = [list() for _ in range( RADIX )]

    for i in lstpositive:
      tmp = int((i / placement) % RADIX)
      buckets[tmp].append(i)

    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        lstpositive[a] = i
        a += 1

    placement *= RADIX
    
    print ("Na de sortering:")
    print (lstpositive)
    print (lstnegative)
    return lst

if __name__ == '__main__':
    lst = [210, -7, -124, 9324, 32, -10]
    print("Dit was de lijst voor de RADIX sortering:")
    print(lst)
    my_sort(lst)
    print("Dit was de lijst na de RADIX sortering:")
    print(lst)
