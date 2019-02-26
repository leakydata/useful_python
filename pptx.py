#Check Shape Type in a slide or slides
for shape in slide.shapes:
  print(shape.shape_type)
  
  
########## CHARTS ##########


## Axes Values
# Maximum Y-Axis Value (the maximun scale)
prs.slides[40].shapes[0].chart.plots[0].chart.value_axis.maximum_scale

# Minimum Y-Axis Value (the minimum scale)
prs.slides[40].shapes[0].chart.plots[0].chart.value_axis.minimum_scale

# X-Axis Labels
tupleOfTuples = prs.slides[40].shapes[0].chart.plots[0].categories.flattened_labels
x_axis_labels = list(sum(tupleOfTuples, ()))
print(x_axis_labels)

# Does the plot axis have Minor Gridlines (boolean: True or False)
prs.slides[40].shapes[0].chart.plots[0].chart.value_axis.has_minor_gridlines

# Does the plot axis have Major Gridlines (boolean: True or False)
prs.slides[40].shapes[0].chart.plots[0].chart.value_axis.has_major_gridlines


## Plot Values
# The chart plot bargraph values
prs.slides[40].shapes[0].chart.series[0].values

# The chart plot values for a stacked bargraph
for s in range(0,len(prs.slides[40].shapes[1].chart.series)):
    print(prs.slides[40].shapes[1].chart.series[s].values)

# Check if chart has legend and list the values
legend = []
if prs.slides[40].shapes[1].chart.has_legend:
    for p in range(0, len(prs.slides[40].shapes[1].chart.plots)):
        for s in range(0, len(prs.slides[40].shapes[1].chart.plots[p].series)):
            print(prs.slides[40].shapes[1].chart.plots[p].series[s].name)
            legend.append(prs.slides[40].shapes[1].chart.plots[p].series[s].name)
    
    
#----------------
# Chart Type
prs.slides[40].shapes[1].chart.chart_type # COLUMN_STACKED (52)
prs.slides[40].shapes[1].chart.chart_type._member_name # COLUMN_STACKED
prs.slides[40].shapes[1].chart.chart_type.real # 52
prs.slides[40].shapes[1].chart.chart_type._docstring # Stacked Column.




#------- Smart Shapes i.e. Diagrams ----------

from bs4 import BeautifulSoup

# Get the rIds of chevrons in Diagram (basically where text is likely to be stored
def get_rIds(slide,shape_num):
    soup = BeautifulSoup(prs.slides[slide].shapes[shape_num].part.rels.xml)
    diagram_rIds = []
    text_data = soup.findAll('relationship', attrs={'target' : re.compile(r'(^\.\./diagrams/drawing[0-9]*\.xml$)')}) 
    for t in text_data:
        diagram_rIds.append(t.get('id'))
    return diagram_rIds
    
# Once you have the text about pull out text and combine subfields (specific to my own work and digrams: we use numbers to label)   
def diagram_text(slide,shape_num,rId):
    data = prs.slides[slide].shapes[shape_num].part.related_parts[rId].blob
    soup = BeautifulSoup(data)
    text_data = soup.findAll('a:t') 

    mydict = {}
    new_list = [n.contents[0] for n in text_data]
    digits = [int(idx+1) for idx, val in enumerate(new_list) if val.isdigit()]

    for idx, i in enumerate(digits):
        if idx != len(digits)-1:
            mydict[new_list[i-1]] = ''.join(new_list[i:i+1])
        else:
            mydict[new_list[i-1]] = ''.join(new_list[i:])
    return mydict


