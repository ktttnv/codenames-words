def remove_new_line_symbol(line):
    return line[:-1] if line[-1] == '\n' else line


def bin_search(lst, target):
    left_ind = 0
    right_ind = len(lst)

    while left_ind < right_ind:
        mid_ind = (left_ind + right_ind) // 2

        if lst[mid_ind] > target:
            right_ind = mid_ind
        else:
            left_ind = mid_ind + 1

    right_ind = right_ind - 1

    if lst[right_ind] == target:
        # return right_ind
        return True

    # return -1
    return False


