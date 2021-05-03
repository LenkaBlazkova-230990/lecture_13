import os
import csv
import matplotlib.pyplot as plt
import math

cwd_path = os.getcwd()
file_path = 'files'


def read_file(file_name):
    """
    Reads csv file from given folder
    :param file_name: (str) the name of csv file
    :return:
    """
    data_points = []
    with open(os.path.join(cwd_path, file_path, file_name), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # skip header
        next(csv_reader)

        # read each row
        for row in csv_reader:
            data_points.append([float(number) for number in row])

    return data_points


def draw_data(data_points, closest_pair=[]):
    """
    Function creates new figure and draw data points into scatter plot.
    :param data_points: (list of lists): each sublist is 1x2 list with x and y coordinate of a point.
    :param closest_pair: (tuple of ints): indices of the closest pair of points, default = empty list
    :return:
    """

    plt.scatter(
        x=[point[0] for point in data_points],
        y=[point[1] for point in data_points],
        color=['blue' if point not in closest_pair else 'red' for point in data_points]
    )
    plt.show()


def closest_pair_BF(array):
    min_dist = math.dist(array[0], array[1])
    point_1 = array[0]
    point_2 = array[1]
    num_points = len(array)

    if num_points == 2:
        return point_1, point_2, min_dist

    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            if i != 0 and j != 1:
                dist = math.dist(array[i], array[j])
                if dist < min_dist:
                    min_dist = dist
                    point_1, point_2 = array[i], array[j]

    return point_1, point_2, min_dist


def closest_split_pair(x_wise, y_wise, minimal_dist, points):
    num_points = len(x_wise)

    mid_point_x = x_wise[num_points //2][0]

    sub_array_y = [point for point in y_wise if mid_point_x - minimal_dist <= point[0] <= mid_point_x + minimal_dist]
    minimal_dist_new = minimal_dist
    len_y = len(sub_array_y)

    for i in range(len_y - 1):
        for j in range(i + 1, min(i + 7,len_y)):
            point_1, point_2 = sub_array_y[i], sub_array_y[j]
            dist = math.dist(point_1, point_2)

            if dist < minimal_dist_new:
                minimal_dist_new = dist
                points = point_1, point_2

    return points[0], points[1], minimal_dist_new


def closest_pair(x_wise, y_wise):
    num_points = len(x_wise)
    middle_idx = num_points // 2

    if num_points <= 3:
        point_1, point_2, their_distance = closest_pair_BF(x_wise)
        return point_1, point_2, their_distance

    left_X = x_wise[:middle_idx]
    right_X = x_wise[middle_idx:]

    mid_point = x_wise[middle_idx][0]
    left_Y = list()
    right_Y = list()

    for point in y_wise:
        if point[0] <= mid_point:
            left_Y.append(point)
        else:
            right_Y.append(point)

    (p1, q1, md1) = closest_pair(left_X, left_Y)
    (p2, q2, md2) = closest_pair(right_X, right_Y)

    if md1 <= md2:
        min_distance = md1
        points = (p1, q1)
    else:
        min_distance = md2
        points = (p2, q2)

    (p3, q3, md3) = closest_split_pair(x_wise, y_wise, min_distance, points)

    if min_distance <= md3:
        return points[0], points[1], min_distance
    else:
        return p3, q3, md3


def main(file_name):
    # read data points
    data_points = read_file(file_name)

    # draw points
    # draw_data(data_points)

    # find the closest pair - BRUTE FORCE
    p1_bf, p2_bf, min_dist_bf = closest_pair_BF(data_points)

    sorted_by_X = sorted(data_points, key = lambda x: x[0])
    sorted_by_Y = sorted(data_points, key = lambda x: x[1])

    # find the closest pair - REKURZIVNE
    p1, p2, min_dist = closest_pair(sorted_by_X, sorted_by_Y)
    print(min_dist)
    print(p1)
    print(p2)

    draw_data(data_points, [p1, p2])


if __name__ == '__main__':
    my_file = 'points.csv'
    main(my_file)
