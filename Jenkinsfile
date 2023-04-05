pipeline {
	agent any
	stages {
	    stage('Fetch code') {
            steps {
               git branch: 'vp-rem', url: 'https://github.com/FullStackArtist/Jenkins.git'
            }

	    }

	    stage('Build'){
	        steps{
	           sh 'python PatternOverlap.py'
	        }

	        post {
	           success {
	              echo 'Now Archiving it...'
	              archiveArtifacts artifacts: '**/target/*.war'
	           }
	        }
	    }
	}
}
