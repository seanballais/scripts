import sys

def main(args):
    boundary_x_orig_top_left = 734.0
    boundary_y_orig_top_left = 11.0
    boundary_width = args[0]
    boundary_height = args[1]

    building_x_orig = args[2]
    building_y_orig = args[3]

    building_x = building_x_orig - boundary_x_orig_top_left
    building_y = building_y_orig - boundary_y_orig_top_left

    building_x = building_x - (boundary_width / 2)
    building_y = building_y - (boundary_height / 2)

    print(f'{building_x}, {building_y}')


if __name__ == '__main__':
    main(sys.argv[1:])
