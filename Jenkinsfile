pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage ('Checkout Git repo'){
            steps {
                checkout scm
            }
        }    
        stage('build') {
            steps {
                echo 'Building the artifact....'
                sh 'python3 /home/ec2-user/python-devops-app/manage.py db init'
                sh 'python3 /home/ec2-user/python-devops-app/manage.py db migrate'
                sh 'python3 /home/ec2-user/python-devops-app/manage.py db upgrade'
        
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }   
        } 


    }
}