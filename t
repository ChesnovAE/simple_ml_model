pipeline {
  agent { 
    docker { 
        image 'python:3.8'
        args '-u root:root'
    }
  }
  stages {
    stage('build') {
      steps {
        sh 'if -d simple_ml; then rm -rf simple_ml;'
        sh 'git clone https://gitlab.com/DataCat/simple_ml.git'
        sh 'cd simple_ml && pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'cd simple_ml && pytest -vv .'
      }   
    }
  }
}