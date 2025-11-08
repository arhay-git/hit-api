pipeline {
    agent any

    stages {
        stage('Debug Test Files') {
            steps {
                sh '''
                echo "=== DEBUG START ==="
                echo "Current directory:"
                pwd
                echo "Files in directory:"
                ls -la
                echo "Test files:"
                find . -name "*test*" -type f
                echo "Content of test_get_user.py:"
                cat test_get_user.py || echo "File not found!"
                echo "=== DEBUG END ==="
                '''
            }
        }
        
        stage('Run API Tests') {
            steps {
                sh '''
                docker run --rm \
                  -v $(pwd):/workspace \
                  -w /workspace \
                  --network jenkins-net \
                  python:3.12-slim \
                  sh -c "pip install pytest requests && python -m pytest --maxfail=1 --disable-warnings -v"
                '''
            }
        }
    }
}