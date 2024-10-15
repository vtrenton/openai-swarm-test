from swarm import Swarm, Agent

client = Swarm()

def back_to_manager():
    return manager

def transfer_to_devops():
    return devops

def transfer_to_neteng():
    return neteng

def transfer_to_netsec():
    return netsec

#def transfer_to_infrasec():
#    return infrasec

def transfer_to_appsec():
    return appsec

manager = Agent(
    name="Manager",
    instructions="You are the manager - introduce yourself and using the provided dockerfile give this to each agent. Once all the other agents have assest the file. Make recommendations based on what their recommendations. Assure you have feedback from all agents before providing report to user.",
    functions=[transfer_to_devops, transfer_to_neteng, transfer_to_netsec, transfer_to_appsec],
)

devops = Agent(
    name="DevOps Engineer",
    instructions="You are a Devops Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices. Then hand off to the next agent",
    functions=[back_to_manager],
)

neteng = Agent(
    name="Network Engineer",
    instructions="You are a Network Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices.",
    functions=[back_to_manager],
)

netsec = Agent(
    name="Network Security",
    instructions="You are a Network Security Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices.",
    functions=[back_to_manager],
)

#infrasec = Agent(
#    name="Infrastructure Security Engineer",
#    instructions="You are an infrastructure security engineer, introduce yourself - assess the dockerfile and deployment manifests and make recommandations.",
#    functions=[back_to_manager],
#)

appsec = Agent(
    name="Application Security Engineer",
    instructions="You are an infrastructure security engineer, introduce yourself - assess the dockerfile and deployment manifests and make recommandations",
    functions=[back_to_manager],
)

response = client.run(
    agent=manager,
    messages=[{"role": "user", "content": '''
# Use the specific Golang version with Alpine to build the application
FROM golang:1.23.1-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the Go module files and download dependencies
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the source code
COPY . .

# Build the Go application
RUN go build -o /kcgen ./cmd/kcgen/kcgen.go

# Use the same image for the final stage to avoid additional layers
FROM golang:1.23.1-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the binary from the builder stage
COPY --from=builder /kcgen .

# Define the entry point to accept command line arguments
ENTRYPOINT ["./kcgen"]'''}],
)

print(response.messages[-1]["content"])
