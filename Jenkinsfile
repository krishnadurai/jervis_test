echo "Pipeline for N-ary Tree"
node {
    stage 'set-up'
    sh "pwd > pwd.current"
    env.WORKSPACE = readFile('pwd.current')
    sh "rm pwd.current"
    
    stage 'checkout'  
    git url: 'git@github.com:krishnadurai/n-ary_builds_test.git'
    
    stage 'unit test'
    sh "nosetests"
    
    stage 'build'
    BUILD_SCRIPT = env.WORKSPACE.trim() + "/build.sh"
    sh "$BUILD_SCRIPT"
}
