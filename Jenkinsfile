pipeline {
  agent any
  stages {
    stage('checkout code') {
      agent any
      steps {
        git(url: 'https://github.com/nikhil-shukla/pytestFramework.git', branch: 'main', credentialsId: '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')
      }
    }

  }
}