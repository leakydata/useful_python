from math import isnan

##if nans are being stored as keys:
# functional
clean_dict = filter(lambda k: not isnan(k), my_dict)

# dict comprehension
clean_dict = {k: my_dict[k] for k in my_dict if not isnan(k)}

##if nans are being stored as values:
# functional
clean_dict = filter(lambda k: not isnan(my_dict[k]), my_dict)

# dict comprehension
clean_dict = {k: my_dict[k] for k in my_dict if not isnan(my_dict[k])}

