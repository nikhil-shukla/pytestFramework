pipeline {

    agent any

    parameters {
        choice(name: 'TEST_ENV', choices: ['prod', 'qa', 'stage'], description: 'Select the environment.')
        choice(name: 'BROWSER', choices: ['chrome-headless', 'edge-headless'], description: 'Provide the browser info.')
        booleanParam(name: 'REPORT', defaultValue: true, description: 'Toggle this value to execute testcases parallely.')
        booleanParam(name: 'PARALLEL', defaultValue: true, description: 'Toggle this value to execute testcases parallely.')
        string(name: 'TAG', defaultValue: '', description: 'Provide the tag to run the tests.')
    }

    stages {
        stage ('Docker Setup') {
            steps {
                script {
                    echo "Building docker image"
                    docker.build("my-image:latest", "-f Dockerfile --build-arg jenkinsUserId=\$(id -u jenkinsgwagent) .")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("my-image:latest").inside {
                        sh "python3 --version"
                        def pytestCommand = "pytest"
                        if (params.BROWSER) {
                            pytestCommand += " --browser=${params.BROWSER}"
                        }
                        if (params.TEST_ENV) {
                            pytestCommand += " --env=${params.TEST_ENV}"
                        }
                        if (params.TAG) {
                            pytestCommand += " -m=${params.TAG}"
                        }
                        if (params.REPORT) {
                            pytestCommand += " --alluredir target/allure-results --clean-alluredir"
                        }
                        if (params.PARALLEL) {
                            pytestCommand += " -n auto"
                        }
                        echo "Running command: ${pytestCommand}"
                        sh pytestCommand
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Publishing Allure report"
            archiveArtifacts 'target/allure-results/'
            allure([
                includeProperties: false,
                jdk: '',
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'target/allure-results']]
            ])
        }
    }
}
