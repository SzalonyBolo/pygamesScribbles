import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

SIDE = 500
DIMENSIONS = 2
EPSILON = 1


def get_random_point(start, stop=None):
    if stop is None:
        start, stop = 0, start
    return (stop - start) * rng.random((DIMENSIONS,)) + start


def get_random_circle():
    pointA = get_random_point(SIDE)
    max_radius = distance_2_closest_side(pointA)
    radius = max_radius * rng.random()
    return (pointA, radius)


def distance_2_closest_side(A):
    return min(min(a, SIDE - a) for a in A)


def euclidian_distance(A, B):
    """Calculates the euclidian distance between two points

    See https://stackoverflow.com/a/1401828/1048781 for details
    """
    return np.linalg.norm(A - B)


def get_line_outside_circle(circle, radius):
    A = B = circle
    while euclidian_distance(A, circle) < radius:
        A = get_random_point(SIDE)
    in_circle = euclidian_distance(B, circle) < radius
    AB_too_close = euclidian_distance(A, B) < EPSILON
    while in_circle and AB_too_close:
        B = get_random_point(SIDE)
        in_circle = euclidian_distance(B, circle) < radius
    line = [A, B]
    return line


def projection(b, a):
    """orthogonal projection of a onto a straight line parallel to b

    See https://en.wikipedia.org/wiki/Vector_projection for further details
    """
    return ((b @ a) / (b @ b)) * b


def orthogonal_projection(A, B, circle):
    """Calculates the orthogonal projection from circle onto the line AB

    See https://stackoverflow.com/a/9368901/1048781 for further details
    """
    AB = B - A
    AC = circle - A
    # projection = AC - AB * ((AB @ AC) / (AB @ AB))
    proj = AC - projection(AB, AC)

    orthogonal_circle_line = circle - proj
    return orthogonal_circle_line


def plot_results(A, B, circle, radius):

    # now make a circle with no fill, which is good for hi-lighting key results
    circle1 = plt.Circle(circle, radius, color="r", fill=False)

    ax = plt.gca()
    ax.cla()  # clear things for fresh plot

    # change default range so that new circles will work
    ax.set_xlim((0, SIDE))
    ax.set_ylim((0, SIDE))
    # some data
    ax.scatter([A[0], B[0]], [A[1], B[1]], color="blue")
    ax.axline(A, B, color="blue")
    ax.scatter([circle[0]], [circle[1]], color="red")
    # key data point that we are encircling
    ax.plot((5), (5), "o", color="y")

    ax.add_patch(circle1)
    plt.show()


def main():
    circle, radius = get_random_circle()
    A, B = get_line_outside_circle(circle, radius)

    proj = orthogonal_projection(A, B, circle)
    if euclidian_distance(circle, proj) < radius:
        print("We have an intersection!")

    plot_results(A, B, circle, radius)


if __name__ == "__main__":

    main()