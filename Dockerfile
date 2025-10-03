# Define base img 
FROM python:3.12.4

# Working dir
WORKDIR /app

# copy requirements
COPY requirements.txt .

# RUN dependencies
RUN pip install --no-cache -r requirements.txt

# copy rest of the applications
COPY . .

# PORT expose
EXPOSE 8000

# Docker img run Command 
CMD ['uvicorn', 'app:app' , "--host" , "0.0.0.0" , "--port", "8000"]