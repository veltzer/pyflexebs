node('generic') {
  stage('init') {
    checkout scm
  }
    
  stage('python') {
        sh '''
        export http_proxy=http://genproxy.amdocs.com:8080
        export https_proxy=$http_proxy
        export no_proxy=127.0.0.1,10.*,.amdocs.com
        export PATH=${HOME}/.local/bin:${PATH}
        
        pip3 install --user --upgrade pip
        pip3 install -r requirements.txt
        pydmt build
        pyinstaller pyflexebs.spec

        curl -v --user 'deploy:PASSWORD' --upload-file dist/pyflexebs-* http://docker-registry-dto.corp.amdocs.com:8081/repository/pypi_private/
       '''
  }
}
