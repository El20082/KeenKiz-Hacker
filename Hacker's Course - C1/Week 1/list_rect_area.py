
#  Get list of lengths and lsit of widths
lengths = [1, 2, 10, 7]
widths = [8, 1, 4, 7]

# Verify length of the list of lengths and the length of the list of widths are the same
if len(lengths) == len(widths):
    # Get list of areas by multiplying list of lengths and list of widths
    areas = []
    for i in range (0, len(lengths)):
        area = lengths[i] * widths[i]
        areas.append(area)
else:
    print("Make sure lists of lengths and widths are the same")