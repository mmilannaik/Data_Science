# Problem 1
# Write a function with the name print_even which takes one argument n.
# This function should print all even numbers starting from 0 up to but not including n.
# This is how the definition is supposed to look:
# def print_even(n):
#    # This is where your code should print
# def print_even(n):
#    if n != 0:
#        for i in range(0, n):
#            if i % 2 == 0:
#                print(i)
#    else:
#        print(end="")


# print_even(0)


# Problem 2
# Write a function with name compound_interest that takes three arguments:
# principle, rate and years in order. the rate is float and years is an integer.
# The function signature should look like the following.
# This function should return the compounded interest a float value.

# def compound_interest(principle, rate, years):
# This is where you code go.
# compute comp_interest
# return comp_interest


def compound_interest(principle, rate, years):
    if principle > 0 and rate > 0 and years > 0:
        interest = 0.0
        x = principle
        old_principle = principle
        for i in range(years):
            interest = (x * rate * 1) / 100
            x = x + interest
        comp_interest = x - old_principle
        return comp_interest
    else:
        return (0)


compound_interest(100, 5, 2)


