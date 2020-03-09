#!/bin/python3




def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if xs[-1] <= 0:
        return None
    LoL = [x for x in xs if x>0]
    val = min(LoL)
    left = 0
    right = len(xs)-1        
    while left <= right:
        mid = (left+right)//2
        if val < xs[mid]:
            right = mid-1
        if val > xs[mid]:
            left = mid+1
        if val == xs[mid]:
            return mid
    return None

def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    left = 0
    right = len(xs)-1
    if len(xs)==0:
        return 0
   
    def greater_than(left,right):   #left index
        mid = (left+right)//2
        if x==xs[mid]:
            if xs[mid-1]>x or mid==0: #want to make sure it's the lowest index possible
                return mid
            else:       #there is an x with a lower index
                right = mid-1
                return greater_than(left,right)
        if left==right:
            return None
        if x<xs[mid]:
            left = mid+1
            return greater_than(left,right)
        if x>xs[mid]:
            right = mid-1
            return greater_than(left,right)

    def less_than(left,right):      #right index
        mid = (left+right)//2
        if x==xs[mid]:
            if mid==len(xs)-1 or xs[mid+1]<x:
                return mid
            else:
                left = mid+1
                return less_than(left,right)
        if left==right:
            return None
        if x<xs[mid]:
            left = mid+1
            return less_than(left,right)
        if x>xs[mid]:
            right = mid-1
            return less_than(left,right)
 
    i = greater_than(left,right)
    j = less_than(left,right)

    if i==None or j==None:
        return 0
    else:
        return j-i+1


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    def minimums(lo, hi):
       m1 = lo + (hi-lo)/4
       m2 = lo + (hi-lo)/2
       if abs(lo-hi) < epsilon: # base case
           return hi
       if f(m1) < f(m2):
           return minimums(lo,m2)
       if f(m1) > f(m2):
           return minimums(m1,hi)
    return minimums(lo,hi)
