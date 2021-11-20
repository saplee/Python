"""Program that creates beautiful pyramids."""


def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '. Pyramid height depends on base length. Lowest floor consists of base-number chars.
    Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") ->
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    make_pyramid(6, 'a') ->
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    :param base: int
    :param char: str
    :return: list
    """
    result = []
    result1 = []
    if base % 2 == 0:
        for number in range(int((base / 2))):
            result.append(char * (base - (2 * number)))
    else:
        for number in range(int((base // 2) + 1)):
            result.append(char * (base - (2 * number)))
    for word in result:
        my_list = []
        for char in word:
            my_list.append(char)
        result1.append(my_list)
    for string in result1:
        amount = base - len(string)
        num = amount // 2
        for number in range(num):
            string.insert(0, ' ')
        for number in range(num):
            string.append(' ')
    return result1[::-1]


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally. If the the pyramid heights are not equal, add empty lines on the top until they are equal.
    join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) ->
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    result = ""
    for row in pyramid:
        for element in row:
            result += element
        if list != pyramid[~0]:
            result += "\n"
    return result


if __name__ == '__main__':
    pyramid_a = make_pyramid(3, "A")
    print(pyramid_a)  # ->
    """
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    """

    pyramid_b = make_pyramid(6, 'a')
    print(pyramid_b)  # ->
    """
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    joined = join_pyramids(pyramid_a, pyramid_b)
    print(joined)  # ->
    """
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    pyramid_string = to_string(joined)
    print(pyramid_string)  # ->
    """
         aa  
     A  aaaa 
    AAAaaaaaa
    """
