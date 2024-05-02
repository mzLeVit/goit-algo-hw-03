import random 


def get_numbers_ticket(min_num, max_num, qntt):
    if min_num <= 0 or max_num >= 1001:
        return []
    elif qntt > max_num:
        return None
    elif max_num - min_num < qntt:
        return None
    lottery = set ()
    while len(lottery) != qntt:
        lottery.add(random.randint(min_num, max_num))
    
    
    return sorted(lottery)
    
    
        
    
lottery_nums = get_numbers_ticket (1, 6, 2)
print (f"Winning numbers are: , {lottery_nums}")