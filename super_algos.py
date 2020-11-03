
def find_min(element):
    """TODO: complete for Step 1"""
    """
        Find the minimum number in the list, if its a non integer or an empty list it should return -1
    """
    
    for i in element:
        if isinstance(i , int) == False:
            return (-1)
    if len(element) == 0:
        return (-1)
    if len(element) == 1:
        return (element[0])
    else:
        num = element[0]
        temp = find_min(element[1:])
        if temp < num:
            num = temp
    return num
num = [24,49,65,17,38,52,75,82,100]


def sum_all(element):
   """TODO: complete for Step 2"""
   """
        Get the sum of all the numbers in a list. If its a non integer or an empty list is should return -1
   """

   for i in element:
       if isinstance(i , int) == False:
           return (-1)
   if len(element) == 0:
       return (-1)
   if len(element) == 1:
       return (element[0])
   else:
       return element[0] + sum_all(element[1:])
num = [249,49,65,17,38,52,75,82,100]


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    """
        returns all the possible strings of length from the character set
    """
    a = len(character_set)
    return(print_length(character_set,"", n, a, []))

def print_length(character_set, prefix, n ,a, temp):
    if (n == 0):
        temp.append(prefix)
        return
    for i in range(a):
        if isinstance(character_set[i], str) == False:
            return []
        newPrefix = prefix + character_set[i]
        print_length(character_set, newPrefix, n - 1, a, temp)
    return(temp)

