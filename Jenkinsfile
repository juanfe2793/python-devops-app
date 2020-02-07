#!groovy

pipeline {

  agent { docker { image 'python:3.7.2' } }
  step([$class: 'WsCleanup'])
  stage "version"
    sh "python --version"
  stage "Checkout Git repo"
    checkout scm
  stage "Build App" 
    echo 'Installing flask...'
    sh "pip install --user -r requirements.txt"
    sh "pwd"
    sh "python3 manage.py db init"
    sh "python3 manage.py db migrate"
    sh "python3 manage.py db upgrade"
    sh "python3 manage.py runserver"
  stage "test"
    sh "python test.py"
  stage "Trigger downstream"
    echo 'parametro'
 
}