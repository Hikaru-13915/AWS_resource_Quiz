docker build -t aws_quiz:0.1 --build-arg http_proxy=$http_proxy --build-arg https_proxy=$https_proxy . 
cd images
unzip png-512.zip