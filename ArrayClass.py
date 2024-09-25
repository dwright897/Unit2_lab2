# YOUR CODE AND HEADING HERE
# Dalton Wright
# 9/24/24
# DynamicArrays
import ctypes
class DynamicArray:
  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)


  def __make_array(self, c):
      """return new array with capacity c"""
      return (c * ctypes.py_object)()

  def __str__(self):
      if self.__n == 0:
          return "[]"

      out = '['
      for i, element in enumerate(self.__A):
          try:
              out += str(element) + ', '
              temp = self.__A[i+1]
          except:
              break
      return out[:-2] + ']'

  def __getitem__(self, k):
    """return element at index"""
    if k <= 0 or k >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[k]
  
  def get_cap(self):
    #Returns the current copacity of the array
    return self.__capacity 

  def __len__(self):
    #Returns the number of elements in the array
    return self.__n

  def append(self, value):
    # add element to the end of an array
    if self.__n == self.__capacity:
      self.__resize(2*self.__capacity)
    self.__A[self.__n] = value
    self.__n+=1

  def __resize(self, new_capacity):
    #resize array capacity to a bigger/doubled capacity:
    new_array = self.__make_array(new_capacity)
    for i in range(self.__n):
      new_array[i] = self.__A[i]
    self.__A = new_array
    self.__capacity = new_capacity




