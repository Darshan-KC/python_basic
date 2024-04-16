# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

import random
import re

def welcome():
    print("\t##########\t WELCOME TO THE GUESSING GAME \t##########")
    print("\t******************************************************")
    print("\t You can help computer guess the number by giving hints. Around 5 more, 5 less than.\n")
    
def compare(com,usr):
    if(com == usr):
        return 1
    else:
        return 0

def user():
    res = input("Help the computer guessing the number : ")

def computer(min,max):
    g =  random.randint(min,max)
    print("Computer guess {}".format(g))
    return g

def response():
    print("Give hint like. 40 more than your guess or 10 less than your guess")
    res = input("Give hint : ")
    if "more" in res or "great" in res or "big" in res:
        op = '+'
    else:
        op = '-'
    numbers = re.findall(r'\d+', res)
    # print(numbers," and operator is ",op)
    # return [int(num) for num in numbers]
    return {
        'num':int(numbers[0]),
        'op':op
    }

def output(count):
    print("\n\t#############\t THANKS FOR GUIDING\t##############")
    print("\t#### Computer guess the correct number in {} attempts. ####".format(count))
if __name__ == "__main__":
    welcome()
    guess = int(input("Enter the guess number : "))
    
    print("\n\t#######\t GAME BEGINS. \t########")
    min = 0
    max = 100
    tem = computer(min,max)
    count = 1
    while(True):
        result = compare(tem,guess)
        if(result):
            break
        try:
            res = response()
            num = res.get('num')
            op = res.get('op')
        except:
            print("!!!\t Invalid hint.\t!!!")
            continue
        if(op == '-'):
            if min < tem - 2*num:
                min = min + num
            max = abs(tem - num) 
               
            # max = max - num
            
        else:
            if max > min + 2*num:
                max = max - num
            min = tem + num
            
            # min = min + num
        
        if(min > max):
            temp = min
            min = max
            max = temp
        tem = computer(min,max)
        count +=1
        print("max = {} and min = {}".format(max,min))
    # compare()
    # compare(tem)
    output(count)