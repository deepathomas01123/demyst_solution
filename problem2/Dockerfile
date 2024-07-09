# Use a base image that includes both Python and OpenJDK
FROM openjdk:11-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python packages
RUN pip3 install faker pyspark

# Command to run your script
CMD ["python3", "anonymize_spark.py"]
