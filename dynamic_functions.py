def check_3Digits(list1):
  #return number in range(100, 1000)
  three_digit_list = []
  for n in list1:
    if n in range(100,1000):
      three_digit_list.append(n)
    else:
       pass  #better than "return False" because if it finds just one number, it will say false, doesn't go through the whole list
  return three_digit_list
     


  #better than "return False" because if it finds just one number, it will say false, doesn't go through the whole list
########################################################################################################################
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.


########################################################################################################################
# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list (stored in the variable numbers) as long as they are greater than 0 and less than 1000, and returns the result of said sum.



########################################################################################################################
# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
