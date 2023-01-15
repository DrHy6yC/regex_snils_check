import re


def check_snils_form(snils):
    is_snils = False
    mathc_snils = re.search(r'\b\d{3}-\d{3}-\d{3}\s\d{2}\b', snils)
    if mathc_snils != None:
        is_snils = True
    return [is_snils, snils];


def check_sum(sum):
    if sum < 100 and sum >= 10:
        sum = str(sum)
    elif sum <= 9:
        sum = "0" + str(sum)
    elif sum == 100 or sum == 101:
        sum = str("00")
    else:
        sum = sum % 101
        if sum < 10:
            sum = "0" + str(sum)
        else:
            sum = str(sum)
    return sum


def check_snils_sum(is_snils, snils):
    if is_snils:
        snils_ints = []
        i = 0
        sum = 0
        snils_parts = re.findall(r'\d', snils)
        while i < len(snils_parts) - 2:
            snils_ints.append(int(snils_parts[i]))
            sum += snils_ints[i]*(9-i)
            i += 1
        is_snils = check_sum(sum) == snils_parts[len(snils_parts) - 2] + snils_parts[len(snils_parts) - 1]
        return is_snils
    else:
        is_snils = False
    return is_snils


if __name__ == '__main__':
    snils = '151-211-537 04'
    is_exit = True
    while True:
        print("Write exit to quit")
        check = input("Input SNILS check: ")
        if check == "exit":
            break
        print(check_snils_sum(is_snils=check_snils_form(check)[0], snils=check_snils_form(check)[1]))