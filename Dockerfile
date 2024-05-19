FROM python:3.9

RUN pip install streamlit

WORKDIR /app

COPY . /app

EXPOSE 8501

CMD streamlit run main.py


