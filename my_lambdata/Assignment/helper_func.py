# Check a dataframe for nulls, print/report them in a nice "pretty" format
import pandas


def train_val_split(split):
    """
    Create a pandas dataframe

    Split data into train, val, test function

    Train/test 80/20
    """
    return split

if __name__ == "__main__":

    df = pandas.DataFrame({
        'a':[11, 42, 26, 9, 29],
        'b':[21, 32, 2, 14, 19],
        'c':[27, 29, 18, 34, 14], 
        'd':[31, 18, 3, 11, 13],
        'e':[41, 15, 36, 7, 20]}
    )
    #print(df.head())

    train = df[df['a'], + df['b'], + df['c']]
    val = df['d']
    test = df['e']

    print(train)
    print(val) 
    print(test)