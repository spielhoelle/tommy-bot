# If using your own Docker image, use the following `FROM` command syntax substituting your image name
FROM jupyter/minimal-notebook

ADD https://github.com/krallin/tini/releases/download/v0.14.0/tini /tini
RUN chmod +x /tini

# If using your own Docker image without jupyter installed:
# RUN pip install jupyter

ENV JUPYTER_TOKEN=acab

EXPOSE 8888
ENTRYPOINT ["/tini", "--"]
# --no-browser & --port aren't strictly necessary. presented here for clarity
# CMD ["jupyter-notebook", "--no-browser", "--port=8888"]
# if running as root, you need to explicitly allow this:
CMD ["jupyter-notebook", "--allow-root", "--no-browser", "--port=8888"]