pipeline {
    agent any

    stages {
        stage('Prepare Test Environment') {
            steps {
                sh '''
                docker cp . python-runner:/workspace
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                docker exec python-runner pip install -r /workspace/requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                docker exec -w /workspace python-runner python -m pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}