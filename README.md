# STEDI-Human-Balance-Analytics-Solution

## Spark and Data Lakes
### Introduction
Spark and AWS Glue allows us to process data from multiple sources, categorize the data, and curate it to be queried in the future for multiple purposes.
The STEDI team wants to build a data lakehouse solution for sensor data that trains a machine learning model. 

As a data engineer on the STEDI Step Trainer team, we needed to extract the data produced by the STEDI Step Trainer sensors and the mobile app, 
and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model.

### Project Details
The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:

1. trains the user to do a STEDI balance exercise;
2. has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
3. has a companion mobile app that collects customer data and interacts with the device sensors.

STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.
Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. 
The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.
The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.
Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

### Project Data
STEDI has three JSON data sources to use:

1. customer
2. step_trainer
3. accelerometer

### Implementation
#### Landing Zone
Landing zone has raw data directly copied from source using DDL Scripts.
Tables :
1. customer_landing 
2. accelerometer_landing

#### Trusted Zone
We have filtered and modified the data according to the requirements and created Trusted tables using 3 glue jobs
Tables :
1. customer_trusted ( Ignoring records where shareWithResearchAsOfDate is blank and joined with serialnumber )
2. accelerometer_trusted
3. step_trainer_trusted

#### Curated Zone
The curated data from the Glue tables is sanitized and only contains only customer data from customer records that agreed to share data, and is joined with the correct accelerometer data,
and created curated tables using a glue job
Table created is : machine_learning_curated
