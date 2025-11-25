#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class Activity: Debugging and Visualization

Created on Sun Nov 23 05:08:50 2025

@author: ys2952
"""


You will use the following code for bug fixes and data visualization.

1.	Fix the bugs by yourselves first, and use CS50 only to find bugs. If you successfully run the code, you will have the bug-free code. 
2.	Draw a visualization using data from either size_counts or season_stats. Use either the matplotlib or seaborn library. You’re allowed to ask CS50 
    to get some ideas on the visualization. Or, refer to the lecture notes on data visualization.


import pandas as pd


path_to_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"
fire = pd.read_csv(path_to_data)
size_counts, season_stats = summarize_area_by_season(fire)

def summarize_area_by_season(df, small_cut=0.0, medium_cut=10.0):
    """
    Summarize forest fires by season and area category.
    
    Input:
        df (data), small_cut (cut score for the small area), medium_cut (cut score for the medium area)
        
    Output:
        size_counts, season_stats
        
    NOTE: This function contains intentional bugs for review.
    """
    season_map = {
        "Dec":"Winter", "Jan":"Winter", "Feb":"Winter", 
        "Mar":"Spring", "Apr":"Spring", "May":"Spring",
        "Jun":"Summer", "Jul":"Summer", "Aug":"Summer",
        "Sep":"Fall", "Oct":"Fall", "Nov":"Fall",
    }

    # Apply season mapping
    df["season"] = df["month"].apply(lambda m: season_map.get(m))

    def area_category(a):
        # Categorize fire size based on area
        if a <= medium_cut:    
            return "medium"
        elif a <= small_cut: 
            return "small"
        else:
            return "large"

    df["area_cat"] = df["area"].apply(area_category)

    # Group 1: Count of fires by season and size category
    size_counts = df.groupby(["season", "area_cat"]).size().reset_index(name="n_fires")

    # Group 2: Basic statistics by season
    season_stats = df.groupby("season")["area"].agg(['count', 'mean', 'median', 'sum'])
    
    
    return season_stats, size_counts

