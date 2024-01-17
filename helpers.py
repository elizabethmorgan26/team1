import pandas as pd
import numpy as np

def get_dataset_range(start_year, end_year):
    datasets = {}
    for i in range(int(start_year), int(end_year)+1):
        data = pd.read_csv(f"resources/stormevents_{i}.csv")
        datasets[i] = data
    # now you access using dataset[2020], for example
    # don't use quotes for accessing because I convert to ints above, could change IDK
    return datasets

# example usage below; uncomment to try
# sets = get_dataset_range(2020, 2021)
# for set in sets.values(): set.value_counts()

# for "set in sets.values()" will allow iteration over each individual dataset in the range
# to access a specific dataset by year: use sets[2020], or whichever year you need

# =============================================
# change a string into a float; account for magnitude of
# the number as represented in the string
def retype_damage_value(value):
    if pd.isna(value):
        return np.nan

    try:
        if isinstance(value, (int, float)):
            return float(value)

        value_str = str(value)
        if not value_str:
            return np.nan

        num_str = value[:-1]
        magnitude = value[-1]

        num = float(num_str)
        
        if magnitude == 'K':
            num *= 1000
        elif magnitude == 'M':
            num *= 1000000
        elif magnitude == 'B':
            num *= 1000000000
    
        return num
    except (ValueError, IndexError):
        return np.nan
    
# ============================================
def retype_tornado_scale(tornado_scale):
    if pd.isna(tornado_scale):
        return np.nan
    
    scale_dict = {
        "F0": 0, "EF0": 0,
        "F1": 1, "EF1": 1,
        "F2": 2, "EF2": 2,
        "F3": 3, "EF3": 3,
        "F4": 4, "EF4": 4,
        "F5": 5, "EF5": 5,
        "FU": -1, "EFU": -1
    }
    return scale_dict[tornado_scale]

# ============================================

# pass in a SINGLE data set, then this function
# will change the type of the damage colums to float
def retype_damage_col(data):
    data.loc[:,"DAMAGE_PROPERTY"] = data["DAMAGE_PROPERTY"].fillna("0.00K")
    data.loc[:,"DAMAGE_CROPS"] = data["DAMAGE_CROPS"].fillna("0.00K")
    data['DAMAGE_CROPS'] = data['DAMAGE_CROPS'].apply(retype_damage_value)
    data['DAMAGE_PROPERTY'] = data['DAMAGE_PROPERTY'].apply(retype_damage_value)


# example usage: sets = get_dataset_range(2020, 2021)
#                for year in sets.keys():
#                   sets[year] = retype_damage_col(sets[year])
    
# ============================================
    
def clean_storm_df(dataFrame, narrow_columns):
    narrow_df = dataFrame[narrow_columns] # reduce columns to relevant ones
    
    # translate tornado F scale into simple integer scale
    narrow_df['TOR_F_SCALE'] = narrow_df['TOR_F_SCALE'].apply(retype_tornado_scale)

    # fill missing values for damage columns
    narrow_df["DAMAGE_PROPERTY"] = narrow_df["DAMAGE_PROPERTY"].fillna("0.00K")
    narrow_df["DAMAGE_CROPS"] = narrow_df["DAMAGE_CROPS"].fillna("0.00K")

    # re-type damage values to float to support math operations
    narrow_df['DAMAGE_PROPERTY'] = narrow_df['DAMAGE_PROPERTY'].apply(retype_damage_value)
    narrow_df['DAMAGE_CROPS'] = narrow_df['DAMAGE_CROPS'].apply(retype_damage_value)

    # merge deaths/injuries/damages columns
    narrow_df["TOTAL DEATHS"] = narrow_df["DEATHS_DIRECT"] + narrow_df["DEATHS_INDIRECT"]
    narrow_df["TOTAL INJURIES"] = narrow_df["INJURIES_DIRECT"] + narrow_df["INJURIES_INDIRECT"]
    narrow_df["TOTAL DAMAGES"] = narrow_df["DAMAGE_PROPERTY"] + narrow_df["DAMAGE_CROPS"]

    # remove now extraneous columns; damages columns remain as we perform individual analyses
    narrow_df = narrow_df.drop(columns=["INJURIES_DIRECT", "INJURIES_INDIRECT","DEATHS_DIRECT", "DEATHS_INDIRECT"])

    # Narrow down events that have had at least one death and/or at least one injury 
    narrow_df = narrow_df.loc[(narrow_df["TOTAL DEATHS"] > 1) | (narrow_df["TOTAL INJURIES"] > 1)]

    # reset the index 
    narrow_df.reset_index(drop=True, inplace=True)

    return narrow_df