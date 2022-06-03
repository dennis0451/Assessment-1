


def optimal_change(item_cost, amount_paid):
##find change
    change_due = abs(item_cost - amount_paid)
    change_in_pennies = change_due * 100
    change_given = []
    final = []

## made a dict of money converted into pennies
    money_in_pennies = {
        '$100 bill' : 10000,
        '$50 bill' : 5000,
        '$20 bill' : 2000,
        '$10 bill' : 1000,
        '$5 bill' : 500,
        '$1 bill' : 100,
        'quarter' : 25,
        'dime' : 10,
        'nickel' : 5,
        'penny' : 1
    }

    plural_bills = {
        '$100 bill' : '$100 bills',
        '$50 bill' : '$50 bills',
        '$20 bill' : '$20 bills',
        '$10 bill' : '$10 bills',
        '$5 bill' : '$5 bills',
        '$1 bill' : '$1 bills',
        'quarter' : 'quarters',
        'dime' : 'dimes',
        'nickel' : 'nickels',
        'penny' : 'pennies'
    }
#iterating though money_in_pennies to determine change, and each denomination to the change_given list
    for key in money_in_pennies:
        while change_in_pennies/money_in_pennies[key] >= 1:
            change_given.append(key)
            change_in_pennies -= money_in_pennies[key]   

#dict or list to determine number of occurences for each denomination
    change_to_return = {}
    dollar_amt = []
    bill_count = []

# sort through change given list and add number of occurences to empty change_to_return dict, and turn dict to list.
    for denomination in change_given:
        if denomination in change_to_return:
            change_to_return[denomination] += 1
        else:
            change_to_return[denomination] = 1
    for key,val in change_to_return.items():#list
        dollar_amt.append(key)
        # print(key)
        bill_count.append(val)

#final logic for return statement

    if item_cost == amount_paid:
        return "No change due."
    elif item_cost > amount_paid:
        return f"You owe ${change_due}."
    else:
        for x in range(0,len(bill_count)-1):  
            if bill_count[x] < 2:
                final.append(str(bill_count[x]))
                final.append(' ')
                final.append(dollar_amt[x])
                final.append(', ')
            else:
                final.append(str(bill_count[x]))
                final.append(' ')
                final.append(plural_bills[dollar_amt[x]])
                final.append(', ')
# #edge case            
    if bill_count[-1] < 2:
        final.append('and ')
        final.append(str(bill_count[-1]))
        final.append(' ')
        final.append(dollar_amt[-1])
             
    else:
        final.append('and ')
        final.append(str(bill_count[-1]))
        final.append(' ')
        final.append(plural_bills[dollar_amt[-1]])
    #return statement     
    return f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {''.join(final)}."

    
print("1:", optimal_change(61, 100) == "The optimal change for an item that costs $61 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, and 4 $1 bills.")
print("2:", optimal_change(33, 100) == "The optimal change for an item that costs $33 with an amount paid of $100 is 1 $50 bill, 1 $10 bill, 1 $5 bill, and 2 $1 bills.")
print("3:", optimal_change(.25, 652) == "The optimal change for an item that costs $0.25 with an amount paid of $652 is 6 $100 bills, 1 $50 bill, 1 $1 bill, and 3 quarters.")
print("4:", optimal_change(16.65, 1526.25) == "The optimal change for an item that costs $16.65 with an amount paid of $1526.25 is 15 $100 bills, 1 $5 bill, 4 $1 bills, 2 quarters, and 1 dime.")
print(optimal_change(50,50))
print(optimal_change(100, 7))
