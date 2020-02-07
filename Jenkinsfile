pipeline {
    agent { docker { image 'python:3.7.1' } }
    
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
                  
                  sh 'pip3 install --user flask flask-migrate flask-script'
                  echo 'Building the artifact....'
                  sh 'python3 manage.py db init'
                  sh 'python3 manage.py db migrate'
                  sh 'python3 manage.py db upgrade'
                }
              
            }
        }    
        stage('test') {
            steps {
                sh 'python test.py'
            }   
        } 


    }
}