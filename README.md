# End-to-End-MLflow-Project
Understanding of End to End MLflow project


"""
Utils: Utils are utility functions for the test suite.
lets say you want to read the yaml file in all of our components, 
so instead of writing the yaml read function in all the files you can keep it inside common.py file.
so whenever you want to read the yaml file, you can import the common.py file and use the function.
"""

"""
ConfigBox : The purpose of config box is to convert the data into class attributes instead of keeping it as a dictionary/ some other data structure.
for example, if you have a dictionary like {'a': 1, 'b': 2}, with a normal dictionary, you can only access the value of 'a' using dict['a'].
but with config box, you can access the value of 'a' using dict.a.

Example code snippet:
from box import ConfigBox
d = {'a': 1, 'b': 2}
print(d.a)                  ### this will raise an error
config = ConfigBox({'a': 1, 'b': 2})   ### this will convert the dictionary into class attributes
print(config.a)  # Output: 1
"""

"""
Ensure Annotations: Ensure annotations is a decorator that ensures that the function has type annotations.
It is used to ensure that the function has type annotations and that the types are correct.
in the below example, though the function add has type mentioned in it as int, 
it will not raise an error if the types are not correct(even if you pass a string it will work).
To overcome this, we can use ensure annotations decorator which will raise an error if the types are not correct.

Example code snippet:
from ensure import ensure_annotations
@ensure_annotations
def add(a: int, b: int) -> int:
    return a + b
add(1, 2)  # Output: 3
add(1, "2")  # Raises TypeError: Expected type 'int' for argument 'b', got 'str' instead. 
             # This error will come only if you use ensure annotations decorator.
"""





## Workflows

1. Update config.yaml  <!-- # created this config file to dwld data from source and extract and save it ins some required folder in project structure -->
2. Update schema.yaml  <!-- #  -->
3. Update params.yaml
4. Update the entity   <!-- # It's a return type of a function, it will return the files of inputs we have given in based on path (her it's paths inside config) -->
5. Update the configuration manager in src config  <!-- # -->
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=entbappy \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model
