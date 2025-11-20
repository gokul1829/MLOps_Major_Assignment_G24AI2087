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

📁 Repository Structure (Detailed & Clear)
mlops-major-project/
│
├── README.md                     # Project documentation
├── .gitignore                    # Ignored files
│
├── train.py                      # Model training script
├── test.py                       # Model testing/accuracy script
├── savedmodel.pth                # Trained model (optional: may be excluded)
│
├── requirements.txt              # Python dependencies
│
├── app.py                        # Flask inference API
│
├── templates/                    # HTML pages for Flask UI
│   ├── index.html                # Image upload page
│   └── result.html               # Prediction result page
│
├── static/
│   └── uploads/                  # Uploaded image storage
│
├── Dockerfile                    # Docker container build instructions
│
├── k8s-deployment.yaml           # Kubernetes deployment + service
│
└── .github/
    └── workflows/
        └── ci.yml                # GitHub Actions CI workflow
