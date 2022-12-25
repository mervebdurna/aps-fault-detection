# APS Sensor Fault Detection Project

[![workflow](https://github.com/mervebdurna/aps-fault-detection/actions/workflows/main.yaml/badge.svg)](https://github.com/mervebdurna/aps-fault-detection/actions/workflows/main.yaml)

# 1. Business Problem 
Air Pressure System failure is common in heavy vehicles and the service and maintenance costs for such failures are high. Therefore, the task at hand is to develop a solution that would help in predicting this failure in trucks to minimize total cost of making false prediction.

Total Cost(metric) = Cost 1 * False Positives + Cost 2 * False Negatives
Cost 1 : An unnecessary check done by a mechanic ($10)
Cost 2 : Missing a faulty truck, which may cause a future breakdown ($500) 


# 2. Data
Data link :  https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks

# 3. Machine Learning Problem
Binary classification problem.
After experimenting different type of pre-processing step and Ml model combinations decided to use Simple Imputer and XGBoost.

# 4. Project Architecture
![image](https://user-images.githubusercontent.com/26697128/209459543-a3709085-d46e-4563-ac32-f3ed8debd19c.png)

# 5. Deployement Architecture
![deployement_flowchart](https://user-images.githubusercontent.com/26697128/209460807-36f04cb8-f8d1-49ce-9137-e6ae0776e778.png)


# 6. Used Technologies
* Python (scikit-learn, pandas, numpy,...)
* MongoDB 
* Git/GitHub
* Git Actions
* Docker
* Airflow
* AWS EC2
* AWS ECR
* AWS S3



