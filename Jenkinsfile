pipeline 
  agent { docker { image 'python:3.7.2' } }
   
  stages {
    stage ('Checkout Git repo'){
      steps {
        checkout scm
      }
    }
    stage('build') {
      steps {
        echo 'Building the artifact....'
        sh 'sudo python3 /home/ec2-user/python-devops-app/manage.py db init'
        sh 'sudo python3 /home/ec2-user/python-devops-app/manage.py db migrate'
        sh 'sudo python3 /home/ec2-user/python-devops-app/manage.py db upgrade'
        sh 'sudo python3 /home/ec2-user/python-devops-app/manage.py runserver -h '0.0.0.0''
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }   
    }
  }
}