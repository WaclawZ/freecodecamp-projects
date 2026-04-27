def verify_card_number(card_number):
    filtered_string = list(filter(lambda c: c.isdigit(), card_number))
    reversed_string = filtered_string[::-1]
    checksum = 0
    for i, num in enumerate(reversed_string):
        num = int(num)
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        checksum += num

    return "VALID!" if checksum % 10 == 0 else "INVALID!"
