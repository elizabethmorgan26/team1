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