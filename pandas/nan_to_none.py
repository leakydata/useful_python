# Change NaN to None
df = df.where(pd.notnull(df), None)

# Change NaN to None
df = df.replace([np.nan], [None])

# Remove them from dicts
def removeNullNoneEmpty(ob):
    l = {}
    for k, v in ob.items():
        if(isinstance(v, dict)):
            x = removeNullNoneEmpty(v)
            if(len(x.keys())>0):
                l[k] = x
        
        elif(isinstance(v, list)):
            p = []
            for c in v:
                if(isinstance(c, dict)):
                    x = removeNullNoneEmpty(c)
                    if(len(x.keys())>0):
                        p.append(x)
                elif(c is not None and c != ''):
                    p.append(c)
            l[k] = p
        elif(v is not None and v!=''):
            l[k] = v
    return l
