# Remove NaNs from a dict
# functional
clean_dict = filter(lambda k: not isnan(my_dict[k]), my_dict)

# dict comprehension
clean_dict = {k: my_dict[k] for k in my_dict if not isnan(my_dict[k])}
