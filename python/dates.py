from datetime import datetime

now = datetime.now()

# dd/mm/YY H:M:S

# 1. Generate the timestamp (Safe for Linux filenames)
#dt_string = now.strftime("%Y%m%d_%H:%M:%S")
# Use %H%M%S instead of %H:%M:%S
dt_string = datetime.now().strftime("%Y%m%d_%H%M%S")
print("date and time =", dt_string)

# ----------------------------------------------------
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
d1 = today.strftime("%Y%m%d")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
