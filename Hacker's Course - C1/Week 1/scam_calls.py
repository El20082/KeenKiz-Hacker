
def get_ints_from_string(str):
    int_list = []
    for c in str:
        c_int = int(c)
        int_list.append(c_int)
    return int_list

phoneNum = input("Please enter a phone number: ")
list = get_ints_from_string(phoneNum)

sum = 0
for i in list:
    sum += i

if sum == 20:
    print("Scam call")
else:
    print("Not a scam call")