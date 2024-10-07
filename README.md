# Matchup Mayhem: Data Mining for Fantasy Cricket

## Overview
The Indian Premier League (IPL) is a renowned Twenty20 cricket league in India, known for its fast-paced, high-stakes matches. Fantasy cricket, a popular pastime among IPL enthusiasts, allows fans to engage deeply with the game by selecting their fantasy teams. The challenge lies in choosing the best 11 players to maximize fantasy points based on player performance in each match. This project leverages data-driven techniques to build a system that optimizes fantasy cricket team selection by analyzing player stats, pitch conditions, and other game-related factors.

<h2><a href="https://youtu.be/1J1K0DyX1gI?si=E4q7pmGNNoxuihkx" target="_blank">Video Presentation Link</a></h2>

## Dataset
We used historical data from IPL matches, including ball-by-ball performances and player career statistics, spanning from 2008 to 2023. The dataset was curated from Kaggle and included player metrics such as:
- Runs scored
- Balls faced
- Strike rate
- Wickets taken
- Economy rate
- Historical match performance

The dataset was split into two main segments:
1. **Player performance for each ball in a match (batsmen and bowlers)**
2. **Player career statistics across seasons**

## Data Architecture
The data architecture comprised two main models:
- A **Performance-Based Scoring Metric Model** using linear regression to predict player performance.
- A **K-means Clustering Model** for in-game player position optimization based on past performance.

![Model Architecture](https://github.com/LaxmikantKabra/cricket-dream-team-prediction/blob/dea16f4a5c37e95d76121458313d594e13ee4f46/img1.jpg)

The pipeline included data collection, preprocessing, feature engineering (such as extracting time-based values), and model training, all executed on historical IPL data.

## Tools Used
- **Python**: For data manipulation, model building, and analysis.
- **Pandas & NumPy**: Data cleaning and manipulation.
- **Scikit-learn**: Machine learning algorithms for linear regression and K-means clustering.
- **Matplotlib & Seaborn**: Data visualization.
- **Kaggle**: Data source for IPL match and player statistics.

## Methods

### Algorithms
1. **Performance-Based Scoring Metric Model**:
   - Built using linear regression.
   - Features included runs, balls faced, wickets taken, economy rate, etc.
   - A custom scoring metric was developed, assigning weights to each feature based on player roles (batsman, bowler, etc.).
   - We used MinMaxScaler to normalize the features, ensuring no feature dominated the model due to its scale.

2. **K-means Clustering**:
   - An unsupervised learning algorithm was used to cluster players based on their in-game roles (batsmen, bowlers, etc.).
   - Features included runs, batting average, wickets, economy, and strike rate.
   - The number of clusters was determined experimentally, yielding 3 clusters for batsmen and 4 clusters for bowlers.

### Result
The linear regression model predicted the top players for a match with an average accuracy of 80%, while the K-means clustering approach had an error margin ranging from 27% to 36%, depending on the match.

## Outcome
The project successfully demonstrated the feasibility of using data-driven methods to predict optimal fantasy cricket team selections. The algorithms are adaptable and provide IPL fantasy players with informed recommendations based on past player performances, ensuring a more competitive and engaging fantasy cricket experience.
