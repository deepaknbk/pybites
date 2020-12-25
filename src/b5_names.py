from collections import defaultdict
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    dedup_names=[]
    title_names=[name.title() for name in names]
    for name in title_names:
        if name not in dedup_names:
            dedup_names.append(name)
    return dedup_names


def last_nm(name):
    return name.split()[1]

def first_nm_len(name):
    return len(name.split()[0])

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names,key=last_nm,reverse=True)
    #pass

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    return sorted(names, key=first_nm_len)[0].split()[0]
    # ...

print("Sorted based on the Sur Name:",sort_by_surname_desc(NAMES))
print("Shortest First Name:",shortest_first_name(NAMES))