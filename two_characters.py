def two_characters(s):

    unique=list(set(s))

    max_len=0

    for i in range(len(unique)):

        for j in range(i+1,len(unique)):

            t=[c for c in s if c==unique[i] or c==unique[j]]

            valid=True

            for k in range(1,len(t)):

                if t[k]==t[k-1]:

                    valid=False

            if valid:

                max_len=max(max_len,len(t))

    return max_len