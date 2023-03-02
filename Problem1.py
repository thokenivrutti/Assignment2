"""Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
def sort_last_elem(num):    #user define function
   return num[-1]   #formula of sorting the last element of give list

def sort_element(my_list):  
   #this method is defined that return a sorted list based on predefine key.
   return sorted(my_list, key=sort_last_elem)

mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("The given list is :")
print(mylist)
print("The sorted list of the last elements is :")
print(sort_element(mylist))