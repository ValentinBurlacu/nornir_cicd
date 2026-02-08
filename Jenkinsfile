pipeline {
    agent any

    environment {
        VENV = "$HOME/jenkins-nornir"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv $VENV || true
                source $VENV/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Validate Configs') {
            steps {
                sh '''
                source $VENV/bin/activate
                python tools/validate_yaml.py
                '''
            }
        }

        stage('Dry Run') {
            steps {
                sh '''
                source $VENV/bin/activate
                python main.py --dry-run
                '''
            }
        }

        stage('Push Config (Main Only)') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                source $VENV/bin/activate
                python main.py --deploy
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Network deployment successful'
        }
        failure {
            echo '❌ Deployment failed'
        }
    }
}
