import sys


def read_circle(filename):
    with open(filename, 'r') as file:
        x, y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return (x, y), radius


def read_points(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points


def comparing_points(center, radius, point):
    x_center, y_center = center
    x_point, y_point = point
    distance_squared = (x_point - x_center) ** 2 + (y_point - y_center) ** 2
    radius_squared = radius ** 2
    if distance_squared == radius_squared:
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Usage: python task2.py <circle_file> <points_file>")
        return
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    center, radius = read_circle(circle_file)
    points = read_points(points_file)
    for point in points:
        position = comparing_points(center, radius, point)
        print(position)


if __name__ == "__main__":
    main()
