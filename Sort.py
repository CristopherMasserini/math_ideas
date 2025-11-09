"""
- For first entry, put it in the back
- Second entry, compare to original first entry. If smaller, it goes in front of that, if larger, it goes behind.
- Third entry, compare to last entry on list. If larger, go behind, if smaller, check with entry in front.
- Continue

EX:
list = [4, 3, 5, 1, 6, 2, 9]
Step 1:
    # Put 4 in the back
    list = [3, 5, 1, 6, 2, 9, 4]
Step 2:
    # Compare 3 to 4
    # 3 less than 4, put 3 ahead of 4
    list = [5, 1, 6, 2, 9, 3, 4]
Step 3:
    # Compare 5 to 4
    # 5 greater than 4, put 5 behind of 4
    list = [1, 6, 2, 9, 3, 4, 5]
Step 4:
    # Compare 1 to 5
    # 1 less than 5, put 1 ahead of 5
    # 1 less than 4, put 1 ahead of 4
    # 1 less than 3, put 1 ahead of 3
    list = [6, 2, 9, 1, 3, 4, 5]
...
"""


def first_entry_to_back(lst: list):
    return lst[1:] + [lst[0]]


def compare_entry(lst: list, entry, maxComps: int):
    print(f"List passed to Compare = {lst}")
    print(f"Entry passed to Compare = {entry}")
    print(f"maxComps passed to Compare = {maxComps}")
    possComp = 1
    while possComp <= maxComps:
        print(f"possComp = {possComp}")
        compValue = lst[-1-possComp]
        print(f"Compare value = {compValue}")
        greater = entry > compValue
        print(f"Greater = {greater}")
        less = entry < compValue
        print(f"less = {less}")
        equal = entry == compValue
        print(f"equal = {equal}")
        print("*"*20)
        possComp+=1


def sort(lst: list):
    print(f"Starting List: {lst}")
    for i, ent in enumerate(lst):
        print(f"i = {i}")
        lst = first_entry_to_back(lst)
        print(f"List after first to back = {lst}")
        if i != 0:
            compare_entry(lst, lst[-1], i)
            print("="*80)
        else:
            print("="*80)


if __name__ == "__main__":
    # listToSort = [5, 2, 6, 1, 4]
    listToSort = [5, 2, 4]
    sort(listToSort)
