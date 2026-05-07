import sys

with open(sys.argv[1], 'r') as ellips_file:
    center_x, center_y, rad_x, rad_y = map(
        int,
        ellips_file.read().split()
    )

with open(sys.argv[2], 'r') as points_file:
    points = [
        list(
            map(int, line.strip().split())
        )
        for line in points_file.readlines()
    ]

eps = 10**(-38)

for point in points:
    x = (point[0] - center_x) / rad_x
    y = (point[1] - center_y) / rad_y

    r2 = x ** 2 + y ** 2
    
    if abs(r2 - 1) < 10**(-40):
        print(0)
    elif r2 < 1:
        print(1)
    else:
        print(2)
        
