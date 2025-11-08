pipeline {
    agent any
    
    stages {
        stage('Copy Test Files') {
            steps {
                sh '''docker exec python-runner mkdir -p /app
                    docker cp . python-runner:/app/
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'docker exec python-runner pip install -r /app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker exec -w /app python-runner python -m pytest --maxfail=1 --disable-warnings -v'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}