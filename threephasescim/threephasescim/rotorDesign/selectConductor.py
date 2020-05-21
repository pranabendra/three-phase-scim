import bisect
import math

def select_conductor(area_given_by_user, matrix_conductor, isCircular):
    if isCircular:
        swg_column = matrix_conductor[:,0]
        diameter_column = matrix_conductor[:,1]
        area_column = matrix_conductor[:,2]

        swg_index = bisect.bisect_right(area_column, area_given_by_user)

        swg_number = swg_column[swg_index]
        area_to_be_used = area_column[swg_index]
        diameter_to_be_used = diameter_column[swg_index]

        return swg_number, area_to_be_used, diameter_to_be_used 
    else:
        all_possible_areas = []
        all_possible_dimensions = []
        for width_index in range(1, 33):
            for thickness_index in range(1, 31):
                if matrix_conductor[width_index][thickness_index] == -1:
                    continue
                else:
                    if matrix_conductor[width_index][thickness_index] > area_given_by_user:
                        all_possible_areas.append(matrix_conductor[width_index][thickness_index])
                        all_possible_areas.append(matrix_conductor[width_index][thickness_index])
                        all_possible_dimensions.append((matrix_conductor[width_index][0], matrix_conductor[0][thickness_index]))
                        all_possible_dimensions.append((matrix_conductor[0][thickness_index], matrix_conductor[width_index][0]))
                        break
        
        return all_possible_areas, all_possible_dimensions
