
FROM python:3.12-slim


WORKDIR /generativeapi


COPY  . /generativeapi
RUN pip install streamlit langchain pypdf
RUN pip install streamlit

EXPOSE 8501


CMD ["streamlit", "run", "frontendapp.py"]
