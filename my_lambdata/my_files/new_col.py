# Single function to take a list, turn it into a series
# and add it to a dataframe as a new column.
from pandas import DataFrame

df = DataFrame({'p/e': [1, 2, 3, 3, 1, 0], 'short': [3, 1, 0, 3, 2, -2],
                'debt': [-1, 0, 1, 1, 4, 3], 'loss': [1, 1, 4, 3, 2, 1],
                'min': [0, 2, 3, 1, 2, 3], 'max': [3, 1, 0, 4, 0, 2],
                'yield': [1, -2, 1, 4, 4, 1], 'loss': [1, 4, 3, 1, 0, 3]})


def new_list(list):

    '''
    Params: Turn our series into a new column.

    Return: outputs a new list.
    '''

    list = pd.Series([4, -2, 0, 3, 1, 1])
    df = df[list]
    return new_list.append(df)

print(new_list)
