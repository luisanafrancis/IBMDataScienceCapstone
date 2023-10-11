# IBMDataScienceCapstone
IBM Data Science Professional Certificate

# EXECUTIVE SUMMARY​
Objective: This project focuses on predicting the successful landing of the Falcon 9 first stage, a pivotal factor in estimating launch costs for SpaceX, ultimately assisting the emerging company, Space Y, in strategizing competitive pricing for their rocket launches.​

Data-Driven Decision Making: This project involves leveraging data science and machine learning to predict first stage reusability, a crucial determinant in cost estimation. By collecting and analyzing relevant data, including mission parameters and historical success rates, the aim is to provide Space Y with predictive insights into reusability.​

Significance of First Stage Reusability: SpaceX's cost-efficiency is driven by reusability, particularly in the Falcon 9 first stage. This initiative drastically reduces launch costs, positioning SpaceX competitively by offering Falcon 9 launches at $62 million, a stark contrast to competitors' prices exceeding $165 million per launch.​

Strategic Edge for Space Y: Armed with accurate predictions on first stage reusability, Space Y can strategically set launch prices, optimize business strategies, and compete effectively with industry giants like SpaceX, catalyzing innovation in the commercial space domain.​

# ​INTRODUCTION
In the current era of commercial space exploration, a multitude of companies are ushering in an era of accessible space travel. Key players like Virgin Galactic, Rocket Lab, Blue Origin, and notably SpaceX, have made significant strides in this domain. SpaceX, in particular, has achieved remarkable feats, including missions to the International Space Station, the development of Starlink satellite internet constellation, and manned space ventures. A significant aspect contributing to SpaceX's success is the cost-effectiveness of their rocket launches. Falcon 9, one of SpaceX's key rocket models, is notably cost-efficient, largely due to its first stage reusability. Understanding the success of landing this first stage is pivotal in determining the cost of each launch, presenting a significant challenge addressed in this capstone.​

Falcon 9 launches, a central focus of this capstone, follow a similar trajectory to traditional rockets. However, what sets them apart is the ability to recover the first stage. This first stage, a critical and costly component of the rocket, sometimes doesn't land successfully, resulting in a crash or strategic sacrifice based on mission parameters such as payload, orbit, and customer requirements. Analyzing and predicting the successful recovery of this first stage holds the key to pricing each launch competitively.​

This capstone project centers on utilizing SpaceX launch data extracted from the SpaceX REST API, particularly focusing on past launch records. The objective is to predict whether SpaceX will attempt to land a rocket, a crucial aspect of their operations. the challenge lies in determining launch prices and predicting first stage reusability, not through conventional rocket science methods, but via data-driven approaches involving machine learning. Gathering insights from public information and utilizing a data-driven approach to determine these critical elements is the primary objective of this project.​

# METHODOLOGY
Data Collection:​
Utilize SpaceX REST API to gather comprehensive launch data.​
Retrieve attributes such as Flight Number, Date, Booster version, Payload mass, Orbit, Launch Site, and Outcome.​

​Data Wrangling:​
Transform JSON API response into a structured, tabular format.​
Address NULL values, specifically in PayloadMass, by calculating and replacing them with the mean.​
Filter and isolate Falcon 9 launches for focused analysis.​
Supplement dataset through web scraping for additional attributes like Grid Fins, Reused, Legs, and more.​

Exploratory Data Analysis (EDA):​
Analyze success rates and trends over time since 2013.​
Explore success rates based on launch sites and payload mass.​
Identify attributes correlated with successful first stage landings.​

Interactive Visual Analytics:​
Build interactive dashboards using Plotly Dash, featuring pie charts and scatter plots.​
Use Folium to calculate distances, plot coordinates, and analyze launch site proximity.​
​
Predictive Analysis:​
* Preprocessing:​ Standardize the data to prepare for model training.​
* Train-Test Split:​ Divide the data into training and testing sets for model evaluation.​
* Model Training and Hyperparameter Tuning:​
Train models: Logistic Regression, Support Vector Machines, Decision Tree Classifier, and K-nearest neighbors.​
Perform Grid Search to find the best hyperparameters for each model.​
* Model Evaluation:​
Evaluate models using the best hyperparameter values on the training data.​
Determine the model with the highest accuracy.​
*Confusion Matrix:​ Output the confusion matrix to assess model performance.​

## Conclusion: Will the first stage land?
In summary, leveraging machine learning to forecast the successful landing of the Falcon 9 first stage, we utilized a dataset of 18 test samples. Our models demonstrated an impressive accuracy score of 0.8, enabling us to reliably predict that, out of the 18 test samples, 12 are likely to result in a successful landing. This predictive capability is a significant stride in optimizing cost estimation and ultimately enhancing the efficiency of rocket launches, a crucial factor in the ever-evolving landscape of space exploration.






​
