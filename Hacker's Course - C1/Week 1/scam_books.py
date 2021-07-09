
def get_ints_from_string(str):
    int_list = []
    for c in str:
        c_int = int(c)
        int_list.append(c_int)
    return int_list

isbn = input("Enter your isbn: ")
list = get_ints_from_string(isbn)

sum = 0
for i in range(0, len(list)):
    if i%2 == 0:
        # Current digit is even
        sum += list[i] * 1
    elif i%2 == 1:
        # Current digit is odd
        sum += list[i] * 3

if sum%10 == 0:
    print("Valid book")
else:
    print("Fake book you are getting scammed")