#!/usr/bin/python3
"""
Function that returns a list of lists of integers representing the Pascal’s
triangle of n
"""

def pascal_triangle(n):
  pascal_triangle = []
  if n > 0:
    for i in range(n):  
      pascal_triangle.append([])  
      pascal_triangle[i].append(1)
      for j in range(1, i):  
        pascal_triangle[i].append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
      
      if i != 0:
        pascal_triangle[i].append(1) 

  return pascal_triangle
