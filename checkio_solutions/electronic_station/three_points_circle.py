# https://py.checkio.org/mission/three-points-circle
from math import acos, degrees, sqrt
from itertools import combinations


def calculate_length(p, q):
    return sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)


def calcuate_angles(a, b, c):
    # Law of cosines: https://en.wikipedia.org/wiki/Law_of_cosines
    cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_b = (a**2 + c**2 - b**2) / (2 * a * c)
    a = round(degrees(acos(cos_a)), 5)
    b = round(degrees(acos(cos_b)), 5)
    c = 180 - a - b
    return (a, b, c)


def is_right_angle(points):
    lines = combinations(points, 2)
    lengths = sorted([calculate_length(l[0], l[1]) for l in lines])
    angles = calcuate_angles(lengths[0], lengths[1], lengths[2])
    return 90 in angles


def calculate_longest_side(points):
    lines = combinations(points, 2)
    longest_line = 0
    longest_point = None

    for line in lines:
        length = calculate_length(line[0], line[1])
        if length > longest_line:
            longest_line = length
            longest_point = line

    return longest_point


def calculate_midpoint(p, q):
    return ((p[0] + q[0])/2, (p[1] + q[1])/2)


def calculate_gradient(p, q):
    return (q[1] - p[1]) / (q[0] - p[0])


def normal_gradient(x):
    return -1 / x


def calculate_right_angle_centre_point(points):
    longest_side_points = calculate_longest_side(points)
    return calculate_midpoint(longest_side_points[0], longest_side_points[1])


def calculate_non_right_angle_triangle_centre_point(points):
    midpoint_1 = calculate_midpoint(points[0], points[1])
    midpoint_2 = calculate_midpoint(points[1], points[2])

    gradient_1 = calculate_gradient(points[0], points[1])
    gradient_2 = calculate_gradient(points[1], points[2])

    bisector_gradient_1 = normal_gradient(gradient_1)
    bisector_gradient_2 = normal_gradient(gradient_2)

    centre_x = ((bisector_gradient_1 * midpoint_1[0]) - (bisector_gradient_2 * midpoint_2[0])
                + midpoint_2[1] - midpoint_1[1]) / (bisector_gradient_1 - bisector_gradient_2)

    centre_y = bisector_gradient_1 * (centre_x - midpoint_1[0]) + midpoint_1[1]

    return (centre_x, centre_y)


def minimal_number(x):
    return "{0}".format(str(int(round(x,2)) if round(x, 2) % 1 == 0 else round(x, 2)))


def checkio(data):
    points = sorted(eval(data))

    if len(points) != 3:
        return "Not enough points"
    elif (len(set(p[0] for p in points)) == 1
         or len(set(p[1] for p in points)) == 1):
        return "All points line on a line"
    elif len(set(p[0] for p in points)) == 2:
        # If two points are on the same horizontal line i.e. x value is the same
        # Then inverse gradient will be infinity
        # Rearrange points to avoid this being calculated
        if points[0][0] == points[1][0]:
            points = [points[0], points[2], points[1]]
        elif points[1][0] == points[2][0]:
            points = [points[1], points[0], points[2]]
    elif len(set(p[1] for p in points)) == 2:
        # If two points are on the same vertical line i.e. x value is the same
        # Then gradient will be infinity
        # Rearrange points to avoid this being calculated
        if points[0][1] == points[1][1]:
            points = [points[0], points[2], points[1]]
        elif points[1][1] == points[2][1]:
            points = [points[1], points[0], points[2]]

    centre_point = calculate_right_angle_centre_point(points) \
                    if is_right_angle(points) \
                    else calculate_non_right_angle_triangle_centre_point(points)

    radius = calculate_length(points[0], centre_point)

    circle_equation = "(x-{x})^2+(y-{y})^2={r}^2".format(
        x=minimal_number(centre_point[0]),
        y=minimal_number(centre_point[1]),
        r=minimal_number(radius))

    return circle_equation


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(7,3),(9,6),(3,6)") == "(x-6)^2+(y-5.83)^2=3^2"
    assert checkio("(9,8),(9,4),(3,6)") == "(x-6.33)^2+(y-6)^2=3.33^2"