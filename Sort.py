"""
- For first entry, put it in the back
- Second entry, compare to original first entry. If smaller, it goes in front of that, if larger, it goes behind.
- Third entry, compare to last entry on list. If larger, go behind, if smaller, check with entry in front.
- Continue

EX:
list = [4, 3, 5, 1, 6, 2, 9]
Step 1:
    list = [3, 5, 1, 6, 2, 9, 4]
Step 2:
    list = [5, 1, 6, 2, 9, 3, 4]
Step 3:
    list = [1, 6, 2, 9, 3, 4, 5]
Step 4:
    list = [6, 2, 9, 1, 3, 4, 5]
...
"""



