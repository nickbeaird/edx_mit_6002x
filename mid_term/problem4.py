


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    best_count = 0
    tentative_list = []

    if len(L) == 1:
        return L[0]

    for i in range(0, len(L)):
        potential_longest = [L[i]]
        potential_count = L[i]
        if potential_count > best_count:
            best_count = potential_count

        for k in range(i + 1, len(L)):
            test = sum(potential_longest) + L[k]
            if max(test, L[k]) != L[k]:
                potential_longest.append(L[k])
            if test > best_count:
                best_count = test
                tentative_list = potential_longest
                
    return best_count


if __name__ == '__main__':
    short_list = [3, 4, -1, 5, -4]
    long_list = [3, 4, -8, 15, -1, 2]
    one_list = [1]
    two_ones = [1, -1]
    # print(max_contig_sum(short_list))
    # print(max_contig_sum(long_list))
    print(max_contig_sum(one_list))
    print(max_contig_sum(two_ones))
