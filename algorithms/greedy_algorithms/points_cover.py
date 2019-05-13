

def points_cover1(points):
    covers = []
    while points:
        xm = min(points)
        covers.append([xm, xm + 1])
        for i in points[:]:
            if i <= xm + 1:
                points.remove(i)

    return len(covers)


def points_cover2(points):
    points = sorted(points)
    i = 0
    n = len(points)
    covers = []
    while i < n:
        l = points[i]
        r = points[i] + 1
        covers.append([l, r])

        i += 1
        while (i < n) and (points[i] <= r):
            i += 1

    return covers


print(points_cover2([0.5, 1, 1.5, 2, 3, 3.5, 4]))
