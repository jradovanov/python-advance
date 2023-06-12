
# variable  | method | dictionary
sorted_data = sorted(shop_dict, key=lambda k: (-len(shop_dict[k]), k))
#                             using function - lambda; with key - k
#                               using len of values to sort for
#                               using minus - "-" to sort in descending order
#                               without minus the sort will be ascending order
# in the end using key - "k" if two len() equal to be ordered in key alphabetically