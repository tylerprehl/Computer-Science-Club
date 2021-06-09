pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Jenkins Minute Pipeline'
      }
    }

    stage('Whatever\'s Next') {
      parallel {
        stage('Whatever\'s Next') {
          steps {
            readFile '\\Competitive Programming\\Practice Problems\\RockPaperScissorsMaster.py'
            pwd()
          }
        }

        stage('Second Print') {
          steps {
            timeout(time: 2, activity: true) {
              echo 'Sup diggity dog'
            }

          }
        }

      }
    }

  }
}