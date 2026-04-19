ARG IMAGE_TAG=24.7.1-2

FROM condaforge/mambaforge:${IMAGE_TAG}

LABEL maintainer="Luis M. Torres-Villegas"

WORKDIR /glauco
COPY environment.yml .

RUN conda config --set channel_priority strict && \
    mamba env create -n glauco_env -f environment.yml

# Make RUN commands use the new environment (see: https://pythonspeed.com/articles/activate-conda-dockerfile/)
SHELL ["mamba", "run", "-n", "glauco_env", "/bin/bash", "-c"]

COPY . .
RUN python setup.py install

# ENTRYPOINT doesn't use the same shell as RUN so you need the conda stuff
ENTRYPOINT ["mamba", "run", "-n", "glauco_env", "python", "-OO", "-m", "glauco"]
