FROM continuumio/miniconda3
WORKDIR /app
COPY . .

RUN conda update conda && \
    conda clean --all && \
    conda create -y -n worker-env && \
    conda install -y -n worker-env -c conda-forge rq && \
    conda clean -y --all

CMD ["conda", "run", "--no-capture-output", "-n", "worker-env", "python", "worker.py"]