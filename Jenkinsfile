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
        stage ('install flask'){
            steps {
              echo 'Installing flask...'
              withEnv(["HOME=${env.WORKSPACE}"]){
                  
                  sh 'pip3 install flask flask-migrate flask-script'
              }
              
            }
        }    
        stage('build') {
            steps {
                echo 'Building the artifact....'
                sh 'python3 manage.py db init'
                sh 'python3 manage.py db migrate'
                sh 'python3 manage.py db upgrade'
                sh  'python3 manage.py runserver'        
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }   
        } 


    }
}