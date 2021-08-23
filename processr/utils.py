import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "Dibetes Negative", 1: "Dibetes Positive"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "no_times_pregant" :d.no_times_pregant,
            "glu_conc" :d.glu_conc,
            "bp" :d.bp,
            "skin_thickness" :d.skin_thickness,
            "insulin" :d.insulin,
            "mass_index" :d.mass_index,
            "diabetes_pedgree" :d.diabetes_pedgree,
            "age" :d.age,
            "dibetes_yn" :d.dibetes_yn
        }
        for d in data
    ]

    return processed
