from swarm import Swarm, Agent

client = Swarm()

def transfer_to_neteng():
    return neteng

def transfer_to_netsec():
    return netsec

def transfer_to_infrasec():
    return infrasec

def transfer_to_appsec():
    return appsec

manager = Agent(
    name="DevOps Engineer",
    instructions="You are the manager - assure the infrastructure code code is sent to each of the Agents and they responnd with recommendations. then pass on to the next agent.",
    functions=[transfer_to_neteng, transfer_to_netsec, transfer_to_infrasec, transfer_to_appsec],
)

devops = Agent(
    name="DevOps Engineer",
    instructions="You are a Devops Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices. Then hand off to the next agent",
)

neteng = Agent(
    name="Network Engineer",
    instructions="You are a Network Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices.",
)

devops = Agent(
    name="Network Security",
    instructions="You are a Network Security Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices.",
)

infrasec = Agent(
    name="Infrastructure Security Engineer",
    instructions="You are an infrastructure security engineer, introduce yourself - assess the dockerfile and deployment manifests and make recommandations.",
    functions=[transfer_to_appsec]
)

appsec = Agent(
    name="Application Security Engineer",
    instructions="You are an infrastructure security engineer, introduce yourself - assess the dockerfile and deployment manifests and make recommandations",
)

response = client.run(
    agent=devops,
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
