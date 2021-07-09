
# Get list of lengths and list of widths
lengths = [1, 5, 2, 7]
widths = [9, 2, 1, 7]

# Verify that the length of the list of lengths and the length of the list of widths are the same
if len(lengths) == len(widths):

    areas = []
    # To find each area: lengths[i] * widths[i]
    for i in range(0, len(lengths)):
        length = lengths[i]
        width = widths[i]
        area = length * width
        areas.append(area)

    # Expected output: areas = [9, 10, 2, 49]
    for i in range(0, len(areas)):
        print(areas[i])

else:
    print("Make sure length of lists are the same")