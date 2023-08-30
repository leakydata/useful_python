# Remove Column Heading Formatting In Excel Export
from pandas.io.formats import excel
excel.ExcelFormatter.header_style = None
