from swarm import Swarm, Agent

client = Swarm()

def transfer_to_neteng():
    return neteng

def transfer_to_netsec():
    return netsec

def transfer_to_infrasec():
    return infrasec

def transfer_to_infrasec():
    return infrasec

devops = Agent(
    name="DevOps Engineer",
    instructions="You are a Devops Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices",
    functions=[transfer_to_neteng],
)

neteng = Agent(
    name="Network Engineer",
    instructions="You are a Network Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices",
    functions=[transfer_to_netsec],
)

devops = Agent(
    name="Network Security",
    instructions="You are a Network Security Engineer, introduce yourself - assess the Dockerfile and deployment manifests and make recommendations around best practices",
    functions=[transfer_to_infrasec],
)

infrasec = Agent(
    name="Infrastructure Security Engineer",
    instructions="You are an infrastructure security engineer, introduce yourself - assess the dockerfile and deployment manifests and make recommandations",
    functions=[transfer_to_appsec]
)

appsec = Agent(
    name="Application Security Engineer",
    instructions="You are an infrastructure security engineer, introduce yourself - assess the dockerfile and deployment manifests and make recommandations",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": ""}],
)

print(response.messages[-1]["content"])
