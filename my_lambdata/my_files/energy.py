import pandas

class energy():
    def __init__(self, source, fuel):
        self.source = source
        self.fuel = fuel
    
    #def DataFrameTransformer(object):
    #    print(self.df.head())

    def solar(self):
        """
        Params Solar energy from 5 level state functions
        """
        solar = {
            "RD90A6": "func01_state",
            "JO63A9": "func02_state",
            "MM31X9": "func03_state",
            "MR29B4": "func04_state",
            "BE74L8": "func05_state"
        }

        #breakpoint()
        
        my_col = self.source["ENERGIZE"]
        other_col = my_col.map(solar)
        self.fuel["SOLAR"] = other_col
        return solar


print(solar('RD90A6'))



















'''
if __name__ == "__main__":

     df = pandas.DataFrame({
        'a':[11, 42, 26, 9, 29],
        'b':[21, 32, 2, 14, 19],
        'c':[27, 29, 18, 34, 14], 
        'd':[31, 18, 3, 11, 13],
        'e':[41, 15, 36, 7, 20]}
    )


transformer = DataFrameTransformer(df)
transformer.inspect_data()
transformer.solar()
'''   