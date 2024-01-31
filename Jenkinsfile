pipeline {
    agent any
    
    tools{
        jdk 'jdk17'
        allure 'allure'
    }
    
   
    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature', url: 'https://github.com/nikhil-shukla/pytestFramework.git'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''python3 --version
                          python3 -m venv venv
                          . venv/bin/activate
                          pip install -r requirements.txt
                          pytest --browser=$BROWSER --alluredir=./allure-results -n auto'''
                }
            }
        }


        stage('Generate Allure Report') {
            steps {
                script {
                    sh 'allure generate -c allure-results -o allure-report'
                    sh 'nohup allure serve allure-report &'
                }
            }
        }
        
        
    }

    post {
        always {
            archiveArtifacts 'allure-report/'
        }
    }
}
