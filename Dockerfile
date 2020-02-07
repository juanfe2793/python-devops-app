FROM python:3.7.2

# Create app directory
RUN mkdir -p $HOME/app
WORKDIR $HOME/app

# Install app dependencies
COPY requirements.txt $HOME/app
RUN pip install -r requirements.txt

# Bundle app source
COPY . $HOME/app

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["python3 manage.py runserver"]