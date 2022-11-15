# from methods_help import method_help
# from functions import function
# from returnStuff import returnS
from Args_Practice import sum_squares, absolute_sum, personal_numbers
from dynamic_functions import check_3Digits, all_positives, sum_less
from function_interactions import reduce_list, throw_dice, toss_coin, luck
# method_help()
# function()
# returnS()
# sum = 526 + 345
result = check_3Digits([55, 99, 600, 78, 120,4950, 333, 558, 404, 23])
print(result)
positive = all_positives([10, 15, 30 , -8])
print(positive)
total = sum_less([200, 32, 50])
print(total)


dice1 = 0
dice2 = 0
dice_rolled = throw_dice(dice1, dice2)
print(dice_rolled)

my_list = ["1", "2", "4", "9", "9"]
new_list = reduce_list(my_list)
print(new_list)

secret_codes =("heads","tails")
coin_flip = toss_coin() 
print("You flipped: " + coin_flip)

final_list = luck(coin_flip, secret_codes)
print(final_list)

print(sum_squares(1, 4, 9))

print(absolute_sum(1, -4, -9))

print(personal_numbers("martin", 34, 5, 55, 5, 555))
