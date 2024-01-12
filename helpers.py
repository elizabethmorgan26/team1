import pandas as pd

def get_dataset_range(start_year, end_year):
    if int(start_year) < 2008:
        print("USER ERROR: START YEAR TOO LOW")
    elif int(end_year) > 2022:
        print("USER ERROR: END YEAR TOO HIGH")
    # datasets = []
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
def retype_damage_value(value_str):
    if (value_str == float('nan')):
        return value_str
    magnitude = value_str[-1]
    num = float(value_str[0:-2])
    if magnitude == 'K':
        num = num * 1000
    elif magnitude == 'M':
        num = num * 1000000
    elif magnitude == 'B':
        num = num * 1000000000
    else:
        num = float(value_str)
    return num

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