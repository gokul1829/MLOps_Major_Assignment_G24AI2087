# MLOps_Major_Assignment_G24AI2087

This project implements a complete end-to-end MLOps workflow for an Olivetti face-classification model. The objective is to demonstrate how machine learning models can be trained, tested, automated, containerized, and deployed using modern MLOps tools.

The workflow includes:

Model Development: Data loading, preprocessing, training, and evaluation using a Decision Tree classifier.

Version Control: Organized into three dedicated branches (main, dev, docker_cicd) following the assignment guidelines.

Continuous Integration: GitHub Actions pipeline automatically installs dependencies, trains the model, and evaluates accuracy for every push.

Containerization: A fully packaged Docker image containing the trained model and Flask inference API.

Deployment: Kubernetes deployment with 3 replicas, ensuring scalability and reliability.

Web Interface: A simple Flask UI that allows users to upload images and receive predictions.

This setup ensures reproducibility, automation, environment consistency, and scalable deployment—all essential pillars of modern MLOps.

MLOps_Major_Assignment_G24AI2087/  
│
├── README.md                     
├── .gitignore                   
│
├── train.py                      
├── test.py                      
├── savedmodel.pth               
│
├── requirements.txt             
│
├── app.py                        
│
├── templates/                   
│   ├── index.html               
│   └── result.html             
│
├── static/
│   └── uploads/                 
│
├── Dockerfile                    
│
├── k8s-deployment.yaml           
│
└── .github/
    └── workflows/
        └── ci.yml                # GitHub Actions CI workflow
