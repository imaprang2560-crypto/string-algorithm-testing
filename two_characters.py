def alternate(s):

    unique = list(set(s))

    max_len = 0

    for i in range(len(unique)):

        for j in range(i+1, len(unique)):

            filtered = [c for c in s if c == unique[i] or c == unique[j]]

            valid = True

            for k in range(len(filtered)-1):

                if filtered[k] == filtered[k+1]:

                    valid = False

                    break

            if valid:

                max_len = max(max_len, len(filtered))

    return max_len