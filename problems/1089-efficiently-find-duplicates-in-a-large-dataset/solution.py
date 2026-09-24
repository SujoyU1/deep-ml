def find_duplicates(records):

    # records: list of hashable items (ints or strings)

    # return a list of values that appear more than once,

    # each listed once, ordered by the position of its second occurrence

    a=[]

    b=[]

    for i in records:

        if i not in a:

            a.append(i)

        elif i not in b:

            b.append(i)

    return b