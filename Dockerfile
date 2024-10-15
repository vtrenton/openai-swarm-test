# Use the Python 3.12 image from Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install dependencies (git, Rust, and Cargo)
RUN apt-get update && \
    apt-get install -y git curl && \
    curl https://sh.rustup.rs -sSf | sh -s -- -y && \
    export PATH="$HOME/.cargo/bin:$PATH" && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Ensure Rust and Cargo are available in the PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Install the application using pip with git+https
RUN pip install git+https://github.com/openai/swarm.git

# Copy the current directory contents into the container at /app
COPY . /app

# Ensure swarm.py is executable
RUN chmod +x /app/openai_swarm.py

# Specify the default command to run when the container starts
CMD ["python3", "./openai_swarm.py"]

