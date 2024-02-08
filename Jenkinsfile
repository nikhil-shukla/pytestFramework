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
                          pytest --browser=$BROWSER --env=$ENV --alluredir=allure-results -n auto'''
                }
            }
        }


        stage('Generate Allure Report') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
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
