def check_triangle(a, b, c):
    if not isinstance(a, (int, float)) \
            or not isinstance(b, (int, float)) \
            or not isinstance(c, (int, float)):
        return False

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b <= c or b + c <= a or a + c <= b:
        return False

    return True


def find_triangle(*args):
    a = args[0]
    b = args[1]
    c = args[2]

    if not check_triangle(a, b, c):
        return 'bad'

    if a == b and b == c:
        return 'equal'

    if a == b or b == c or c == a:
        return 'bedr'

    return 'usual'
