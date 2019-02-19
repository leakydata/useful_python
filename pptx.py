#Check Shape Type in a slide or slides
for shape in slide.shapes:
  print(shape.shape_type)
  
  
########## CHARTS ##########

## Axes Values
# Maximum Y-Axis Value (the maximun scale)
prs.slides[40].shapes[0].chart.plots[0].chart.value_axis.maximum_scale

# Minimum X-Axis Value (the minimum scale)
prs.slides[40].shapes[0].chart.plots[0].chart.value_axis.minimum_scale

#X-Axis Labels
tupleOfTuples = prs.slides[40].shapes[0].chart.plots[0].categories.flattened_labels
x_axis_labels = list(sum(tupleOfTuples, ()))
print(x_axis_labels)

## Plot Values
# The chart plot bar values
prs.slides[40].shapes[0].chart.series[0].values

# The chart plot values for a stacked bargraph
for s in range(0,len(prs.slides[40].shapes[1].chart.series)):
    print(prs.slides[40].shapes[1].chart.series[s].values)

