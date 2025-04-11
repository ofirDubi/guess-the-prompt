# write a script to build the docker images in respect to the current directory
cd gtp-client
echo 'building client...'
./build_docker.sh
cd ..
echo 'building server...'
cd gtp-server
./build_docker.sh
