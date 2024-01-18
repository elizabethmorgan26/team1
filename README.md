# Storm Data Analysis
This project investigated storm trends over the most recent 15 years. We looked at the storms with the greatest impact overall and then specifically tornados. A comparison between these recent storm impacts was made to the earliest 15 years of the dataset. The project also includes an exploration and analysis of what storm data can tell us about larger weather patterns, such as El Nino and La Nina. 

# Project Description
The Storm Data Analysis project looks to answer three specific research questions:
1. What has been the impact of storms over recent years? Is there a correlation between storm fatalities and total damages? What are the differences in storm impacts between the most recent 15 years and the initial 15 years?
1. Given that tornadoes are one of the most frequent event types and among the most destructive and deadly in our dataset, do tornadoes with greater magnitudes result in increased property damage?
1. Can we answer any larger related questions? For example, can we observe the effects of larger weather patterns in this dataset (i.e. El Nino / La Nina)? 

# Dependencies
The following libraries were used in one or more code files:
* Matplotlib, pandas, numpy, scipy, hvplot

# The Dataset
Authors downloaded .csv files from the National Centers for Environmental Information. (n.d.). Storm Events Database. https://www.ncdc.noaa.gov/stormevents/ftp.jsp
The authors used a subset of the datafiles, specifically years 2008 to 2022/23 and 1950 to 1964. These .csv data files can be found in the Resources folder in main. 
The dataset includes detailed information regarding major storm events in the United States (and territories) and includes a variety of details regarding each storm event, including: 
* Time and location
* Type and severity - category, magnitude, tornado scale
* Damage, injuries, casualties (direct vs indirect, crop vs property damage)
* Data source (trained spotter, public, emergency manager, law enforcement, etc.)

# Repository Contents
In general, you can replicate our work by running our Jupyter notebook files and observing the results. Not all notebooks were used in our final presentation or analysis, but were included to preserve the full efforts of our team. Below are the files important to our final presentation and any special steps required to run them.
- You can view some data exploration and the cleaning process by opening this file: Storm_Analysis.ipynb. This is the primary dataset that authors worked on to answer their research questions.
- Research question one was explored by Kevin, Mandy and David. 
    - What has been the impact of storms over recent years?
        - Kevin explored and analyzed data on the most recent 15 years. He also investigated the types of storms with greatest impact over this time period. The analysis file can be found here: 2008-2022_Analysis_Overview.ipynb
        - Mandy explored the top 5 deadliest storms in the most recent 15 years. She analyzed the relationship between total deaths and total cost of damage for storms over this time period. The analysis file can be found in the main branch here: 2008-2022 Storm Analysis.ipynb
        - David explored the differences in storm impacts between the most recent 15 years and the initial 15 years. Specifically, he compared the occurrences of storms by type as well as total deaths for these time periods. The analysis file can be found here: “1950-1964_df.ipynb”
        - Note: running “1950-1964_df.ipynb” requires moving the all CSV files in "Resources" to the folder there containing that year. For example, you must move all data from 1950 to 1964 to the folder "1950-1964", and the same for recent years. Once finished, move the CSV files back out to the "Resources" folder.
    - Research question two was analyzed by Elizabeth. Tornadoes were one of the most frequent event types and among the most destructive and deadly in our dataset, thereby, Elizabeth conducted a deep analysis of tornadoes. Specifically, she investigated whether the size of the tornado creates more costly damages. The analysis file can be found here: “Tornado_Analysis.ipynb”
    - Research question three was analyzed by Kerim. He analyzed whether the data had a greater impact on weather patterns. Specifically, he explored El Nino and La Nina weather patterns across different regions. The analysis file can be found in Kerim’s branch here: “nino_nina_questions.ipynb”
    - A synopsis of the findings and their implications were crafted in a written summary located in the main branch: Written Summary. The authors also present the findings in a Google slide deck. Each research question is summarized with findings and implications. The authors explore limitations, lessons learned, and areas for further research. The slide deck can be viewed in the main branch as well as on Google drive here: Storm Data Analysis Slide Deck.
    - Any visualizations of data used in the final presentation are found in the folder named "Visualizations"
# Support Functions 
Authors created different functions to streamline the analysis process. These functions can be found in the main branch here: "helpers.py"
# Authors
Kerim Celik, Mandy Cisler, Elizabeth Morgan, Kevin Nazario, David Robles
