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