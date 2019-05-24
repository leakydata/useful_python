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

# Remove NaNs in a dict
import simplejson

clean_dict  = simplejson.loads(simplejson.dumps(my_dict, ignore_nan=True))
## or depending on your needs
clean_dict  = simplejson.loads(simplejson.dumps(my_dict, allow_nan=False))
