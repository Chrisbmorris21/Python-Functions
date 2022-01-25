def convert_to_binary(prm1):
    _bits_needed = 1
    _start = 1
    _user_value = int(prm1)
    _original_in = str(_user_value)
    _binary_value = ""

    """ Loop through the numbers from 1 increasing by
        a power of 2 until we get a number that is equal
        to or exceeds the users input. Increase bit
        counter for each number needed """

    while _user_value > _start:
        _bits_needed = _bits_needed + 1
        _start = _start * 2

    """ When the user value is not equal to a result of a
        multiplication, roll back to previous multiplication
        as it will cause an erroneous bit value at the beginning
        of the binary number. e.g. 31 will create a 32 value erroneously """

    if _user_value != _start:
        _bits_needed = _bits_needed - 1
        _start = _start / 2

    for x in range(_bits_needed):

        if _user_value >= _start:
            _user_value = _user_value - _start
            _binary_value = _binary_value + "1"
            _start = _start / 2
        else:
            _binary_value = _binary_value + "0"
            _start = _start / 2

    """ Break the loop and work out whether or not the final
        digit of the binary number should be 0 or 1 """

    if _start == 1:
        if _start / _user_value == 1:
            _binary_value = _binary_value + "1"
        else:
            _binary_value = _binary_value + "0"

    if _binary_value == "":
        _binary_value = 0

    return _binary_value


def get_ip_address():
    print("What is the IP address?")
    _user_input = input() + "."
    _group_dict = []
    _temp = str("")
    _binary_ip = ""
    """Split the IP address into multiple clusters. Perform the function on each function individually."""
    for i in range(len(_user_input)):
        if _user_input[i].isnumeric():
            _temp = _temp + str(_user_input[i])
        else:
            _group_dict.append(_temp)
            _temp = str("")
    for i in range(len(_group_dict)):
        _preceding_zeroes = 8 - len(str(convert_to_binary(_group_dict[i])))
        for j in range(_preceding_zeroes):
            _binary_ip = _binary_ip + str("0")
        _binary_ip = _binary_ip + str(convert_to_binary(_group_dict[i])) + "."

    return _binary_ip.rstrip(".")


running = True

while running:

    print(get_ip_address())
