FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip uninstall streamlit
RUN pip install --user --upgrade  streamlit matplotlib plotly seaborn \
streamlit-embedcode streamlit-bokeh-events st-annotated-text  \
plotnine smart-open convertdate streamlit-vega-lite pydeck
RUN pip install keras
RUN pip install tensorflow
RUN pip install mlrun
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]