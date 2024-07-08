import sys


def generate_array(n):
    return list(range(1, n + 1))


def generate_intervals(circular_array, n, m):
    intervals = []
    index = 0
    while True:
        interval = []
        for _ in range(m):
            interval.append(circular_array[index])
            index = (index + 1) % n
        intervals.append(interval)
        if interval[-1] == circular_array[0]:
            break
        index = (index - 1) % n
    return intervals


def generate_path(intervals):
    path = [interval[0] for interval in intervals]
    return path


def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    circular_array = generate_array(n)
    intervals = generate_intervals(circular_array, n, m)
    path = generate_path(intervals)
    print(''.join(map(str, path)))


if __name__ == "__main__":
    main()
