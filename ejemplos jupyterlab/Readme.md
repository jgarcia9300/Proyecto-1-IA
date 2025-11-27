docker pull jupyter/datascience-notebook:x86_64-ubuntu-22.04
docker run -p 8888:8888 \
    -v "$(pwd):/home/jovyan/work" \
    jupyter/notebook

docker run -p 8888:8888 \
    -v "$(pwd):/home/jovyan/work" \
    jupyter/scypi-notebook

docker run -p 8888:8888 -v "$(pwd):/home/jovyan/work"  jupyter/notebook

docker run -p 8888:8888 -v "D:\UNIVALLE\NOVENO SEMESTRE\Inteligencia Artificial:/home/jovyan/work" jupyter/scipy-notebook