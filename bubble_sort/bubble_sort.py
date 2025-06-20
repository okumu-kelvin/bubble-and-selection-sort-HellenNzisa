def bubble_sort(unsorted_list):
    n = len(unsorted_list)

    swapped = False

    for i in range(n):
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swap if the element found is greater than the next element
                unsorted_list[j], unsorted_list[j + 1] = (
                    unsorted_list[j + 1],
                    unsorted_list[j],
                )
                swapped = True

        if not swapped:
            # If no two elements were swapped by inner loop, then break
            break

    return unsorted_list
