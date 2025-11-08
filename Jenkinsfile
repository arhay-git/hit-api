pipeline {
    agent any

    stages {
        stage('Run API Tests') {
            steps {
                sh '''
                docker run --rm \
                  -v $(pwd):/workspace \
                  -w /workspace \
                  --network jenkins-net \
                  python:3.12-slim \
                  sh -c "pip install pytest requests && python -m pytest --maxfail=1 --disable-warnings -q"
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