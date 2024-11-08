# End to End Text-Summarizer


...

## Workflows

1. Update config.yaml file
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py

# How to run?

### STEPS:

Clone the repository

'''bash
https://github.com/Vimlesh-17/Text-Summarizer
'''

### STEP 01- Create a conda env after cloning the repo

'''bash
conda create -n {env name} python==3.11.9 -y
'''

'''bash
conda activate {env name}
'''

### STEP 02- install all dependencies
'''bash
pip install -r requirements.txt
'''

'''bash
python app.py
'''

Now,
'''bash
open up your local host and port
'''



'''bash
Author: Vimlesh Chouhan
Data Scientist
Email: Vimleshchouhan8885@gmail.com
'''

# AWS-CICD_Deployment-with-GitHub-Actions

## 1. Login to AWS console

## 2. Create IAM user for deployment

        #with specific access

        1. EC2 access: It is virtual machine
        2. ECR: Elastic Container registry to save your docker image in aws

        #Description: About the deployment

        1. Build docker image of the source code

        2. Push your docker image to ECR

        3. Launch your EC2

        4. Pull your image from ECR in EC2

        5. Launch your docker image in EC2

        #Policy:

        1. AmazonEC2ContainerRegistryFullAcess

        2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image
    - Save the URI: 585008062649.dkr.ecr.us-east-2.amazonaws.com/texts


## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

        #optional
        
        sudo apt-get update -y
        
        sudo apt-get upgrade
        
        #required

        curl -fsSL https://get.docker.com -o get-docker.sh

        sudo sh get-docker.sh

        sudo usermod -aG docker ubuntu

        newgrp docker

## 6. Configure EC2 as self-hosted runner:

        #setting > actions > runner > new self hosted runner > choose os > then run command one after another


## 7. Setup GitHub secrets:

        AWS_ACCESS_KEY_ID=

        AWS_SECRET_ACCESS_KEYS=
        
        AWS_REGION = 

        AWS_ECR_LOGIN_URI = 

        ECR_REPOSITORY_NAME = simple-app