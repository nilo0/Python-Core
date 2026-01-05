# Conditional Logic: 
## Applying indentation and boolean and expression to creates a code block, by if, elif, and else. 
## -> Truthy and falsy values, note that type(bool('hello')) or type(bool(5)) returns True value. 
## -> Falsy values are: None, False, 0, 0.0, 0j, Decimal(0), empty list, dictionary, tuple, string, set bytes and ranges (range(0))
## -> Falsy objects which returns False or 0 are: 
###      - obj.__bool__() 
###      - obj.__len__()

## Terany Operator
condition = True
ternary_operator = "operation is allowed" if condition else "operation is not allowed"
print(ternary_operator)

# ->  Note: == vs is:
##  - is checks if two values are assigned to similar place in memory thus, [] is []) returns False.
##  - == checks if two values are equal thus [] == [] would be True.
