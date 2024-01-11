"""

In Python, a string of text can be aligned left, right and center.

#####.ljust(width)#####

This method returns a left aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  

#####.center(width)#####

This method returns a centered string of length width.

>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----

####.rjust(width)####

This method returns a right aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank

-----Task------

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

##### Input Format #####

A single line containing the thickness value for the logo.

Constraints

The thickness must be an odd number.

###### Output Format #####

Output the desired logo.

####### Sample Input ##########3

5

####### Sample Output ########

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 

"""

if __name__ == "__main__":
    n = int(input())
    h_block = 'H' * n
    sp_block = ' ' * n
    bd_line = h_block + (sp_block * 3) + h_block
    ct_line = (h_block * 5)

    # top triangle
    for ii in range(1, n * 2 + 1, 2):
        print(("H" * ii).center(2 * n - 1, ' '))

    # top body
    for _ in range(n + 1):
        print(bd_line.center(n * 6 - 1, ' '))

    # middle band
    for _ in range(n // 2 + 1):
        print(ct_line.center(n * 6 - 1, ' '))

    # bottom body
    for _ in range(n + 1):
        print(bd_line.center(n * 6 - 1, ' '))

    # bottom triangle
    for ii in range(n * 2 - 1, 0, -2):
        print(("H" * ii).center(n * 10, ' '))



