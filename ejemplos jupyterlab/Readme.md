docker pull jupyter/datascience-notebook:x86_64-ubuntu-22.04
docker run -p 8888:8888 \
    -v "$(pwd):/home/jovyan/work" \
    jupyter/notebook

docker run -p 8888:8888 -v "$(pwd):/home/jovyan/work"  jupyter/notebook