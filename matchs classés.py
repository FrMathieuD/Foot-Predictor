#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:54:14 2024

@author: mathieu
"""

import numpy as np
import pandas as pd
import os 

Team_game_result = pd.read_csv("Team_game_result.csv")
I = ["Home_Team","Away_Team","Result"]
Team_game_result=Team_game_result[I]
T = Team_game_result.to_numpy()

    
debut_lien = "/Users/mathieu/Documents/IMT M2/Projet P5 - Foot Predictor/Base de données/Matrices_Team/"
fin_lien = ".npy"

for i in range(T.shape[0]):
    lien_home = debut_lien + T[i,0] + fin_lien 
    lien_away = debut_lien + T[i,1] + fin_lien 
    Matrice = np.zeros((6,4,20))
    with open(lien_home, 'rb') as f:
        Home = np.load(f)
    with open(lien_away, 'rb') as f:
        Away = np.load(f)
    Matrice[0:3,0:4,0:20] = Home
    Matrice[3:6,0:4,0:20] = Away
    with open(f"/Users/mathieu/Documents/IMT M2/Projet P5 - Foot Predictor/Base de données/Matchs classés/{int(T[i,2])}/{i}.npy", 'wb') as f:
        np.save(f, Matrice)  
    
    