"""
The idea here is that to accurately compare two populations,
you have to normalize how the populations are distributed.

For example, you want to see if cases of heart disease are actually on the rise. You want to compare
2025 levels to 1925 levels. Obviously the population distribution is different, so to compare, they need
to be similar. (If people generally died younger previously and we see people living longer now, is it fair)
to say cases are on the rise, when more people are being afflicted just because there are more people
of that age.

What we do is have the two distributions.
In older population group, we find the age group with the highest count.
That age group in the newer population will be the maximum,
    every other age group that is higher than that gets trimmed to that level.
Then we adjust every other age group in the new population.

For example:
Our maximum age group is 30-39 year olds.
We see in the old population, 0-9 year olds are 10% the size of 30-39 year olds in the old population.
    Our new 0-9 population is to be 10% the 30-39 age group in new population.
        To do this, we do n=0.1*(# of 30-39 yea olds).
        If # of 0-9 year olds > n, we randomly sample 0-9 year olds to remove until we are at that number.
        If # of 0-9 year olds < n, we duplicate 0-9 year olds to fill that number.
            We essentially keep duplicating the group until we just go over n, then randomly sample to remove
            until we are at n.

We do this for every age group. This will make our new population sample fit the distribution of the
old population (and the percentages should still work).
"""




if __name__ == "__main__":
    pass
