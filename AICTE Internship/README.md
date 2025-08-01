# EV Adoption Forecasting

## Project Overview

This project focuses on forecasting Electric Vehicle (EV) adoption trends using machine learning. As EV adoption continues to grow, urban planners and infrastructure developers need accurate forecasts to plan charging stations and related infrastructure effectively.

## Given Details By Raghunandan sir (Mentor)

As electric vehicle (EV) adoption surges, urban planners need to anticipate infrastructure needs—especially charging stations. Inadequate planning can lead to bottlenecks, impacting user satisfaction and hindering sustainability goals.

**Problem Statement:** Using the electric vehicle dataset (which includes information on EV populations, vehicle types, and possibly historical charging usage), create a model to forecast future EV adoption. For example, predict the number of electric vehicles in upcoming years based on the trends in the data.

**Goal:** Build a regression model that forecasts future EV adoption demand based on historical trends in EV growth, types of vehicles, and regional data.

**Dataset:** This dataset shows the number of vehicles that were registered by Washington State Department of Licensing (DOL) each month. The data is separated by county for passenger vehicles and trucks.

- Date: Counts of registered vehicles are taken on this day (the end of this month). - 2017-01-31
  2024-02-29
- County: This is the geographic region of a state that a vehicle's owner is listed to reside within. Vehicles registered in Washington
- State: This is the geographic region of the country associated with the record. These addresses may be located in other
- Vehicle Primary Use: This describes the primary intended use of the vehicle.(Passenger-83%, Truck-17%)
- Battery Electric Vehicles (BEVs): The count of vehicles that are known to be propelled solely by an energy derived from an onboard electric battery.
- Plug-In Hybrid Electric Vehicles (PHEVs): The count of vehicles that are known to be propelled from energy partially sourced from an onboard electric battery
- Electric Vehicle (EV) Total: The sum of Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs).
- Non-Electric Vehicle Total: The count of vehicles that are not electric vehicles.
- Total Vehicles: All powered vehicles registered in the county. This includes electric vehicles.
- Percent Electric Vehicles: Comparison of electric vehicles versus their non-electric counterparts.

## Problem Statement

Using historical electric vehicle registration data from Washington State, this project develops a model to forecast future EV adoption rates. The model predicts the number of electric vehicles in upcoming years based on historical trends, vehicle types, and regional data.

# Week 1:

## Theory and Concepts

### Basic Statistical Concepts

1. **Central Tendency Measures**

   - **Mean**: Average of all values (sum/count)
   - **Median**: Middle value when data is ordered
   - **Mode**: Most frequently occurring value
   - Use Case: Median is preferred when data has outliers as it's less sensitive

2. **Data Distribution**

   - **Normal Distribution**: Bell-shaped curve, symmetric around mean
   - **Skewness**: Measure of distribution asymmetry
   - **Kurtosis**: Measure of whether data is heavy-tailed or light-tailed

3. **Outliers**
   - Definition: Data points that significantly differ from other observations
   - Detection Methods:
     a. **IQR Method**: Uses quartiles (Q1, Q3)
     b. **Z-score Method**: Distance from mean in standard deviations
   - Treatment Methods:
     a. **Removal**: Delete outlier rows (if few)
     b. **Capping**: Set to min/max acceptable values
     c. **Transformation**: Log, square root to reduce impact
     d. **Binning**: Group values into categories

### Libraries Overview

1. **Pandas**

   - Data manipulation library
   - Key Features:
     - DataFrame structure for tabular data
     - Data cleaning and preprocessing
     - File I/O (CSV, Excel, SQL)
     - Group operations and merging

2. **NumPy**

   - Numerical computing library
   - Features:
     - Multi-dimensional arrays
     - Mathematical operations
     - Linear algebra
     - Random number generation

3. **Matplotlib & Seaborn**

   - Data visualization libraries
   - Common Plots:
     - Line plots: Time series data
     - Scatter plots: Relationships
     - Histograms: Distribution
     - Box plots: Outlier detection

4. **Scikit-learn**
   - Machine learning library
   - Components:
     - Preprocessing tools
     - Model selection
     - Classification/Regression
     - Model evaluation

### Data Preprocessing Techniques

1. **Missing Value Handling**

   - Methods:
     a. **Deletion**: Remove rows/columns
     b. **Mean/Median Imputation**: Replace with average
     c. **Forward/Backward Fill**: Use adjacent values
     d. **Prediction**: Use ML to predict missing values

2. **Feature Scaling**

   - **Standardization**: (x - mean)/std
   - **Normalization**: (x - min)/(max - min)
   - **Robust Scaling**: Using quartiles
   - When to use:
     - Required for distance-based algorithms
     - Needed when features are on different scales

3. **Encoding Categorical Variables**
   - **Label Encoding**: Convert to numbers (0,1,2...)
   - **One-Hot Encoding**: Binary columns for each category
   - **Target Encoding**: Replace with target mean
   - Choose based on:
     - Number of categories
     - Ordinal vs nominal data
     - Model requirements

## Dataset Description

The dataset contains monthly electric vehicle registration data from the Washington State Department of Licensing (DOL), covering the period from January 2017 to February 2024.

### Key Features:

- **Date**: End-of-month vehicle registration counts
- **County**: Geographic region within Washington State
- **Vehicle Primary Use**: Primary intended use (Passenger: 83%, Truck: 17%)
- **Battery Electric Vehicles (BEVs)**: Count of fully electric vehicles
- **Plug-In Hybrid Electric Vehicles (PHEVs)**: Count of plug-in hybrid vehicles
- **Electric Vehicle (EV) Total**: Sum of BEVs and PHEVs
- **Non-Electric Vehicle Total**: Count of non-electric vehicles
- **Total Vehicles**: All registered vehicles in the county
- **Percent Electric Vehicles**: Ratio of electric to non-electric vehicles

Dataset Source: [Electric Vehicle Population Size 2024 (Kaggle)](https://www.kaggle.com/datasets/sahirmaharajj/electric-vehicle-population-size-2024/data)

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/Pabitra-Sahoo/EV-Adoption-Forecasting-AICTE.git
cd EV-Adoption-Forecasting-AICTE
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

## Technical Requirements

- Python 3.12.8
- Required Libraries:
  - pandas: Data manipulation and analysis
  - numpy: Numerical computing
  - matplotlib: Data visualization
  - seaborn: Statistical data visualization
  - scikit-learn: Machine learning algorithms
  - joblib: Model persistence

# Week 2:

## Theory and Concepts

### Data Type Handling

1. **Numeric Conversion**

   - Converting string data to numeric types
   - Handling mixed data types
   - Managing conversion errors using error handlers

2. **Date-Time Processing**
   - Converting string dates to datetime objects
   - Extracting temporal features (year, month)
   - Creating time-based aggregations

### Feature Engineering

1. **Lag Features**

   - Creating time-shifted versions of variables
   - Rolling means and averages
   - Percentage change calculations
   - Growth slope computation

2. **Temporal Features**
   - Months since start calculation
   - Cumulative sums and rolling metrics
   - Trend and seasonality extraction

### Model Selection and Evaluation

1. **Random Forest Regression**

   - Ensemble learning principles
   - Decision tree fundamentals
   - Feature importance analysis
   - Hyperparameter tuning concepts

2. **Time Series Concepts**

   - Temporal dependency
   - Seasonality patterns
   - Trend analysis
   - Forecasting principles

3. **Performance Metrics**
   - Mean Absolute Error (MAE)
   - Root Mean Square Error (RMSE)
   - R-squared (R²) interpretation
   - Model validation techniques

### Visualization and Analysis

1. **Time Series Plotting**

   - Historical vs forecast visualization
   - Trend line plotting
   - Cumulative growth charts

2. **Model Insights**
   - Feature importance visualization
   - Prediction vs actual comparisons
   - County-wise growth patterns
   - Regional adoption trends

This theoretical foundation supports understanding both the implementation details and the interpretation of results in EV adoption forecasting.
