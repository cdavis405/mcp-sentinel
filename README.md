
# MCP Sentinel

> **Zero-Touch Enterprise Infrastructure. One Conversation.**

## Overview

**MCP Sentinel** isn't just automation—it's a full-stack enterprise IT environment, architected, deployed, and operated entirely through conversation with an LLM. No clicking through GUIs. No copy-pasting configs. No Terraform plans to review. You describe what you want, and it builds it.

Built on [xorrkaz/cml-mcp](https://github.com/xorrkaz/cml-mcp) as a foundation, MCP Sentinel pushes the boundaries of what's possible when you combine Large Language Models with enterprise infrastructure. From **Windows Group Policy to SD-WAN**, from **RADIUS authentication to certificate auto-enrollment**, from **employee laptop provisioning to Day 2 troubleshooting**—this project covers the entire stack.

### The Vision

Complete enterprise IT. Every layer. Every integration. One conversation.

| Layer | What We're Building |
|-------|---------------------|
| **Identity & Access** | Active Directory, Group Policy, RADIUS, 802.1X, PKI |
| **Network Access Control** | Cisco ISE: authentication, authorization, posture, profiling |
| **Network Infrastructure** | SD-WAN (Cisco vManage/vEdge), MPLS, routing, switching, wireless |
| **Security** | Firewalls, TrustSec, micro-segmentation, zone-based policies |
| **Endpoint** | Certificate enrollment, laptop onboarding, compliance validation |
| **Operations** | LLM-driven troubleshooting, drift detection, automated remediation |

**The scenario:** A new employee receives their laptop. They plug into the network. 802.1X triggers EAP-TLS. RADIUS validates their certificate against Active Directory. ISE returns their authorization profile—VLAN, SGT, downloadable ACL. Group Policy applies their desktop configuration. SD-WAN routes their Teams call over the optimal path. And when something breaks? You ask the LLM to figure out why.

---

## 🎯 The Challenge: Bleeding-Edge Goals

These aren't just features—they're challenges. Some of these push into territory where documentation is sparse and success isn't guaranteed. That's the point.

| Goal | Difficulty | Why It's Hard |
|------|------------|---------------|
| **Full 802.1X with EAP-TLS** | 2x🔥 | Certificate-based auth requires CA, templates, auto-enrollment, supplicant config—all orchestrated |
| **ISE + TrustSec SGTs** | 4x🔥 | Dynamic segmentation based on identity; requires ISE, switch config, and matrix policies |
| **SD-WAN Fabric from Scratch** | 4x🔥 | vManage, vBond, vSmart, certificates, OMP, control policies—all configured via LLM |
| **Zero-Touch Employee Onboarding** | 5x🔥 | The holy grail: laptop connects → authenticated → authorized → configured → optimized |
| **LLM-Driven Troubleshooting** | 4x🔥 | "Why can't Sarah authenticate?" → LLM queries ISE, AD, switch, returns root cause |
| **Cross-Domain Policy Correlation** | 5x🔥 | Trace a policy decision across AD → ISE → Switch → Firewall → SD-WAN |

> **The benchmark:** If an experienced enterprise architect would need a week to set this up manually, MCP Sentinel should do it in a conversation.

---

## 🛡️ Change Management: The Core Philosophy

*Inspired by [The Phoenix Project](https://itrevolution.com/product/the-phoenix-project/).*

Automation without governance is chaos. MCP Sentinel is built on the principle that **no change happens without understanding, visibility, and approval.**

### Every Change. Every Time.

Before any network modification, MCP Sentinel will:

1. **🎯 Blast Radius Analysis** — What could break? Which users, applications, and services are affected?
2. **📋 Command Preview** — The exact commands that will execute, on which devices, in what order
3. **⚠️ Risk Assessment** — Quantified risk level with plain-English explanation
4. **✋ Explicit Confirmation** — Nothing runs until you approve it

```
┌─────────────────────────────────────────────────────────────────────┐
│  PROPOSED CHANGE: Update OSPF Area on Chicago Branch Router         │
├─────────────────────────────────────────────────────────────────────┤
│  BLAST RADIUS:                                                      │
│    • 47 users at Chicago branch will lose connectivity for ~30 sec  │
│    • Voice traffic will failover to backup MPLS path                │
│    • No impact to other branches                                    │
├─────────────────────────────────────────────────────────────────────┤
│  COMMANDS TO EXECUTE:                                               │
│    router ospf 1                                                    │
│      no network 10.5.0.0 0.0.255.255 area 0                         │
│      network 10.5.0.0 0.0.255.255 area 5                            │
├─────────────────────────────────────────────────────────────────────┤
│  RISK: MEDIUM                                                       │
│  Reason: Brief connectivity loss during OSPF reconvergence          │
├─────────────────────────────────────────────────────────────────────┤
│      Proceed with this change? [Yes / No / More Info]               │
└─────────────────────────────────────────────────────────────────────┘
```

### 🔮 The Endgame: Multi-Stakeholder Approval

*This is where it gets interesting.*

The future isn't just you and an AI. It's a **group conversation**—a Slack channel, a Teams chat—where the AI is a participant alongside humans. Everyone who needs to know, knows. Everyone who needs to approve, approves.

**The scenario:**

```
┌─────────────────────────────────────────────────────────────────────┐
│  #chicago-network-maintenance                                       │
├─────────────────────────────────────────────────────────────────────┤
│  🤖 MCP Sentinel                                                    │
│  Proposed: Core switch firmware upgrade at Chicago branch           │
│  Window: Saturday 5:00 AM - 7:00 AM CST                             │
│  Blast Radius: Full site offline during upgrade (~45 min)           │
│  Risk: LOW (tested in lab, rollback plan ready)                     │
│                                                                     │
│  Awaiting approval from: @chris (IT), @marcus (Site GM)             │
├─────────────────────────────────────────────────────────────────────┤
│  👤 Marcus (Site GM)                                                │
│  What's the risk if we don't do this?                               │
├─────────────────────────────────────────────────────────────────────┤
│  🤖 MCP Sentinel                                                    │
│  Current firmware has 3 known CVEs. Vendor support ends in 60 days. │
│  Risk of delayed upgrade: MEDIUM-HIGH                               │
├─────────────────────────────────────────────────────────────────────┤
│  👤 Marcus (Site GM)                                                │
│  Approved ✅. Adding @ryker from HR.                                │
│  @ryker - can you shift the Saturday morning crew to start at 7:30? │
├─────────────────────────────────────────────────────────────────────┤
│  👤 Ryker (HR Manager)                                              │
│  Done. Updated the schedule. You're clear for 5-7 AM.               │
├─────────────────────────────────────────────────────────────────────┤
│  👤 Chris (IT Manager)                                              │
│  Approved ✅                                                        │
├─────────────────────────────────────────────────────────────────────┤
│  🤖 MCP Sentinel                                                    │
│  All approvals received. Change scheduled for Sat 5:00 AM CST.      │
│  Notifications will be sent 24hr and 1hr before maintenance.        │
└─────────────────────────────────────────────────────────────────────┘
```

**This is where AI agents in group chats become transformative.** The AI isn't just executing—it's facilitating cross-functional coordination, answering stakeholder questions in real-time, and ensuring nothing happens without the right approvals.

> **Status:** Some of this isn't possible yet. Group chat AI agents with multi-party approval workflows are emerging technology. But this is the endgame, and MCP Sentinel is being built with this architecture in mind.

### Foundation: cml-mcp

This project builds upon the excellent [cml-mcp](https://github.com/xorrkaz/cml-mcp) by [@xorrkaz](https://github.com/xorrkaz), which provides the core MCP server implementation for Cisco Modeling Labs. We extend this foundation with:

- **Enterprise topology templates** - Pre-built designs for common enterprise architectures
- **Multi-system orchestration** - Coordinate across AD, ISE, network devices, and more
- **Complex dependency management** - Handle startup ordering and service dependencies
- **Infrastructure-as-conversation** - Natural language to production-ready infrastructure

## Core Features (from cml-mcp)

- **Create Lab Topologies:** Tools for creating new labs and defining network topologies
- **Query Status:** Tools to retrieve status information for labs, nodes, and the CML server
- **Control Labs and Nodes:** Tools to start and stop labs or individual nodes as needed
- **Manage CML Users and Groups:** Tools to list, create, and delete local users and groups
- **Run Commands on Devices:** Using [PyATS](https://developer.cisco.com/pyats/), execute commands on virtual devices within CML labs

## Extended Features (MCP Sentinel)

- **Enterprise Topology Deployment:** Deploy complete enterprise networks from YAML definitions
- **Windows Server Integration:** Domain controllers, DNS, DHCP, Group Policy, Enterprise CA
- **Cisco ISE Deployment:** Full ISE configuration—policies, profiling, posture, RADIUS
- **SD-WAN Orchestration:** vManage, vBond, vSmart, and edge deployment
- **End-to-End Validation:** Automated testing of the complete employee experience

---

## 🚧 Current Status

> **Active Development** — Building toward the bleeding-edge goals. Core infrastructure working. The hard stuff is next.

| Component | Status | Notes |
|-----------|--------|-------|
| CML MCP Server (base) | ✅ Working | Foundation from cml-mcp |
| Lab Topology Deployment | 🔄 In Progress | YAML-based definitions |
| Active Directory | 📋 Planned | DCs, DNS, DHCP, GPOs |
| Enterprise CA + 802.1X | 🎯 Challenge | Certificate-based authentication |
| Cisco ISE | 🎯 Challenge | Full NAC deployment |
| SD-WAN Fabric | 🎯 Challenge | Complete overlay network |
| Zero-Touch Onboarding | 🔥 Bleeding Edge | The ultimate validation |
| LLM Troubleshooting | � Bleeding Edge | Day 2 operations via conversation |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              LLM (Claude, etc.)                             │
│                    "Deploy my enterprise network with 3 branches"           │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              MCP Sentinel                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────────┐  │
│  │ Topology Engine │  │ Template Library│  │ Deployment Orchestrator     │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           cml-mcp (Foundation)                              │
│              MCP Server Implementation for Cisco Modeling Labs              │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                         Cisco Modeling Labs (CML)                          │
│                                                                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ Datacenter   │  │     WAN      │  │  Branch 1    │  │  Branch N    │    │
│  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │    │
│  │  │  ISE   │  │  │  │ MPLS   │  │  │  │Router  │  │  │  │Router  │  │    │
│  │  │   DC   │  │  │  │ SD-WAN │  │  │  │Switch  │  │  │  │Switch  │  │    │
│  │  │  FW    │  │  │  └────────┘  │  │  │  AP    │  │  │  │  AP    │  │    │
│  │  └────────┘  │  │              │  │  └────────┘  │  │  └────────┘  │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 🗺️ Roadmap

### Phase 1: Foundation ✅
- [x] Fork and customize cml-mcp
- [x] Basic lab deployment via MCP
- [x] YAML topology definitions

### Phase 2: Identity & Access (Current)
- [ ] **Active Directory Infrastructure**
  - Windows Server domain controllers
  - DNS/DHCP integrated with AD
  - Group Policy Objects (GPOs)
  - Organizational Units structure
  - User/group provisioning

- [ ] **Certificate Services**
  - Enterprise CA deployment
  - Certificate templates for 802.1X
  - Auto-enrollment configuration

### Phase 3: Network Access Control
- [ ] **Cisco ISE Deployment**
  - ISE node deployment and configuration
  - RADIUS server setup
  - 802.1X authentication policies
  - Authorization profiles
  - Posture assessment policies

- [ ] **Network Authentication**
  - Wired 802.1X on switches
  - Wireless 802.1X on controllers
  - MAB fallback for legacy devices
  - Guest access portal

### Phase 4: Network Infrastructure
- [ ] **SD-WAN Fabric**
  - vManage, vBond, vSmart controllers
  - vEdge/cEdge deployment at sites
  - Overlay tunnel configuration
  - Application-aware routing

- [ ] **Underlay Network**
  - MPLS backbone simulation
  - Internet transport simulation
  - Routing protocols (OSPF/BGP)
  - QoS policies

- [ ] **Branch Infrastructure**
  - Branch routers and switches
  - Wireless controllers and APs
  - Local DHCP/DNS relay

### Phase 5: Security & Segmentation
- [ ] **Firewall Integration**
  - Perimeter firewalls
  - Internal segmentation
  - Zone-based policies

- [ ] **Network Segmentation**
  - VLAN design and implementation
  - SGT (Security Group Tags) with TrustSec
  - Micro-segmentation policies

### Phase 6: Employee Onboarding Flow
- [ ] **Complete End-to-End Flow**
  - Employee laptop issued → connects to network
  - 802.1X authentication via EAP-TLS
  - RADIUS validates against Active Directory
  - ISE returns authorization (VLAN, SGT, ACL)
  - Group Policy applies user configurations
  - SD-WAN optimizes application traffic
  - Full connectivity validated

### Phase 7: Day 2 Operations
- [ ] **LLM-Driven Management**
  - Troubleshooting via conversation
  - "Why can't this user authenticate?"
  - Configuration drift detection
  - Automated remediation
  - Change management workflows

---

## 💬 Example Prompts

Here are examples of what MCP Sentinel will enable:

### Full Enterprise Deployment
```
"Build me a complete enterprise environment:
- Headquarters with 2 domain controllers, enterprise CA, and Cisco ISE
- SD-WAN fabric with vManage, vBond, and vSmart
- 3 branch offices connected via SD-WAN
- 802.1X authentication on all wired and wireless ports
- Configure Group Policy for employee laptops
- Set up the complete employee onboarding flow"
```

### Identity Infrastructure
```
"Deploy the identity stack:
- Primary and secondary domain controllers
- Configure DNS and DHCP with AD integration
- Set up an Enterprise CA for certificate-based authentication
- Create OUs for IT, Engineering, Sales, and Contractors
- Build GPOs for each department with appropriate restrictions"
```

### Network Access Control
```
"Configure ISE for network access control:
- Deploy ISE in a 2-node cluster
- Set up RADIUS authentication for all switches
- Create policies: employees get full access, 
  contractors get internet-only, guests hit captive portal
- Enable posture assessment - block non-compliant endpoints
- Configure profiling to identify device types"
```

### Employee Experience
```
"Walk me through the employee onboarding flow:
- A new employee's laptop connects to the network
- Show me how 802.1X authenticates them against AD
- Verify ISE applies the correct authorization policy
- Confirm Group Policy pushes their configurations
- Test that their traffic routes correctly over SD-WAN"
```

### Troubleshooting (Day 2)
```
"Sarah from Engineering can't connect to the network. 
Check ISE for her authentication attempts, verify her 
AD account status, check if her certificate is valid, 
and tell me what's blocking her access."
```

### Current Working Examples (via cml-mcp)
These work today using the underlying cml-mcp functionality:

- "Create a new CML lab called 'Enterprise Test'"
- "Add two IOL routers and connect them with a switch"
- "Start the lab and show me the status of all nodes"
- "Run 'show ip route' on router1"

---

## Requirements

- Python 3.12+
- Cisco Modeling Labs (CML) 2.9 or later
- PyATS (optional; used for device CLI command execution)
- The [uv](https://docs.astral.sh/uv/) Python package/project manager

## Windows Requirements

If you do not want to run CLI commands on devices running in CML, you don't need to do anything else other than install the base `cml-mcp` package.  However,
if you want full support, Windows users also require either Windows Subsystem for Linux (WSL) with Python and `uv` installed within WSL or a Docker environment running on the Windows machine.

## Getting Started

You have several options to run this server, depending on your needs and platform:

### Option 1: Standard I/O (stdio) Transport

This is the traditional way to run the server, where it communicates directly with the MCP client via standard input/output streams.

#### Using uvx (Easiest - No CLI Support)

The easiest way is to use `uvx`, which downloads the server from PyPi and runs it in a standalone environment.  This works for Linux, Mac, and Windows users but does **not** provide CLI command support.  Edit your client's config and add something like the following.  This example is for Claude Desktop:

```json
{
  "mcpServers": {
    "Cisco Modeling Labs (CML)": {
      "command": "uvx",
      "args": [
        "cml-mcp"
      ],
      "env": {
        "CML_URL": "<URL_OF_CML_SERVER>",
        "CML_USERNAME": "<USERNAME_ON_CML_SERVER>",
        "CML_PASSWORD": "<PASSWORD_ON_CML_SERVER>"
      }
    }
  }
}
```

In order to execute CLI commands on devices running within CML, Linux and Mac users will need to change the "args" to `cml-mcp[pyats]`.  For example:

```json
{
  "mcpServers": {
    "Cisco Modeling Labs (CML)": {
      "command": "uvx",
      "args": [
        "cml-mcp[pyats]"
      ],
      "env": {
        "CML_URL": "<URL_OF_CML_SERVER>",
        "CML_USERNAME": "<USERNAME_ON_CML_SERVER>",
        "CML_PASSWORD": "<PASSWORD_ON_CML_SERVER>",
        "PYATS_USERNAME": "<DEVICE_USERNAME>",
        "PYATS_PASSWORD": "<DEVICE_PASSWORD>",
        "PYATS_AUTH_PASS": "<DEVICE_ENABLE_PASSWORD>"
      }
    }
  }
}
```

The additional `PYATS` environment variables are needed to let the MCP server know how to login to those running devices.

Windows users that want CLI command support and are using Windows Subsystem for Linux (WSL) should configure:

```json
{
  "mcpServers": {
    "Cisco Modeling Labs (CML)": {
      "command": "wsl",
      "args": [
        "uvx",
        "cml-mcp[pyats]"
      ],
      "env": {
        "CML_URL": "<URL_OF_CML_SERVER>",
        "CML_USERNAME": "<USERNAME_ON_CML_SERVER>",
        "CML_PASSWORD": "<PASSWORD_ON_CML_SERVER>",
        "PYATS_USERNAME": "<DEVICE_USERNAME>",
        "PYATS_PASSWORD": "<DEVICE_PASSWORD>",
        "PYATS_AUTH_PASS": "<DEVICE_ENABLE_PASSWORD>",
        "WSLENV": "CML_URL/u:CML_USERNAME/u:CML_PASSWORD/u:PYATS_USERNAME/u:PYATS_PASSWORD/u:PYATS_AUTH_PASS/u:PYATS_AUTH_PASS/u"
      }
    }
  }
}
```

Windows (and really Mac and Linux users, too) that want CLI command support and are using Docker should configure:

```json
{
  "mcpServers": {
    "Cisco Modeling Labs (CML)": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--pull",
        "always",
        "-e",
        "CML_URL",
        "-e",
        "CML_USERNAME",
        "-e",
        "CML_PASSWORD",
        "-e",
        "PYATS_USERNAME",
        "-e",
        "PYATS_PASSWORD",
        "-e",
        "PYATS_AUTH_PASS",
        "xorrkaz/cml-mcp:latest"
      ],
      "env": {
        "CML_URL": "<URL_OF_CML_SERVER>",
        "CML_USERNAME": "<USERNAME_ON_CML_SERVER>",
        "CML_PASSWORD": "<PASSWORD_ON_CML_SERVER>",
        "PYATS_USERNAME": "<DEVICE_USERNAME>",
        "PYATS_PASSWORD": "<DEVICE_PASSWORD>",
        "PYATS_AUTH_PASS": "<DEVICE_ENABLE_PASSWORD>"
      }
    }
  }
}
```

#### Using FastMCP CLI

An alternative is to use FastMCP CLI to install the server into your favorite client.  FastMCP CLI supports Claude Desktop, Claude Code, Cursor, and manual JSON generation.  To use FastMCP, do the following:

1. Clone this repository:

    ```sh
    git clone https://github.com/xorrkaz/cml-mcp.git
    ```

1. Change directory to the cloned repository.

1. Run `uv sync` to install all the correct dependencies, including FastMCP 2.0.  **Note:** on Linux and Mac, run `uv sync --all-extras` to get CLI command support.

1. Create a `.env` file with the following variables set:

    ```sh
    CML_URL=<URL_OF_CML_SERVER>
    CML_USERNAME=<USERNAME_ON_CML_SERVER>
    CML_PASSWORD=<PASSWORD_ON_CML_SERVER>
    # Optional in order to run commands
    PYATS_USERNAME=<DEVICE_USERNAME>
    PYATS_PASSWORD=<DEVICE_PASSWORD>
    PYATS_AUTH_PASS=<DEVICE_ENABLE_PASSWORD>
    ```

1. Run the FastMCP CLI command to install the server.  For example:

    ```sh
    fastmcp install claude-desktop src/cml_mcp/server.py:server_mcp --project `realpath .` --env-file .env
    ```

### Option 2: HTTP Transport (Streaming)

The server now supports HTTP streaming transport, which is useful for running the MCP server as a standalone service that can be accessed by multiple clients or when you want to run it in a containerized or remote environment. This mode uses HTTP Server-Sent Events (SSE) for real-time communication.

#### Running the HTTP Server

To run the server in HTTP mode, set the `CML_MCP_TRANSPORT` environment variable to `http`. You can also configure the bind address and port.

First, install the package:

```sh
uv venv
source .venv/bin/activate
uv pip install cml-mcp # or cml-mcp\[pyats] to get CLI command support
```

Or for development, clone the repository and sync dependencies:

```sh
git clone https://github.com/xorrkaz/cml-mcp.git
cd cml-mcp
uv sync # add --all-extras to get CLI command support
```

Then run the server using `uvicorn`:

```sh
# Set environment variables
export CML_URL=<URL_OF_CML_SERVER>
export CML_MCP_TRANSPORT=http
export CML_MCP_BIND=0.0.0.0  # Optional, defaults to 0.0.0.0
export CML_MCP_PORT=9000     # Optional, defaults to 9000

# Run the server with uvicorn
uvicorn cml_mcp.server:app --host 0.0.0.0 --port 9000
```

Or create a `.env` file with these settings:

```sh
CML_URL=<URL_OF_CML_SERVER>
CML_MCP_TRANSPORT=http
CML_MCP_BIND=0.0.0.0
CML_MCP_PORT=9000
```

Then run:

```sh
cml-mcp
```

The server will start and listen for HTTP connections at `http://0.0.0.0:9000`.

#### Authentication in HTTP Mode

When using HTTP transport, authentication is handled differently than stdio mode:

- **CML Credentials**: Instead of being set via environment variables, CML credentials are provided via the `X-Authorization` HTTP header using Basic authentication format.
- **PyATS Credentials**: For CLI command execution, PyATS credentials can be provided via the `X-PyATS-Authorization` header (Basic auth) and the enable password via the `X-PyATS-Enable` header

Example headers:

```http
X-Authorization: Basic <base64_encoded_cml_username:cml_password>
X-PyATS-Authorization: Basic <base64_encoded_device_username:device_password>
X-PyATS-Enable: Basic <base64_encoded_enable_password>
```

#### Configuring MCP Clients for HTTP

To use the HTTP server with an MCP client, you'll need to use the `mcp-remote` tool to connect to the HTTP endpoint. Most MCP clients like Claude Desktop don't natively support HTTP streaming, so `mcp-remote` acts as a bridge between the client (which expects stdio) and the HTTP server.  This bridge requires [Node.js](https://nodejs.org/en/download/) to be installed
on your client machine.  Node.js includes the `npx` utility that allows you to run Javascript/Typescript applications in
a dedicated environment.

Add the following configuration to your MCP client config (e.g., Claude Desktop's `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "Cisco Modeling Labs (CML)": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "http://<server_host>:9000/mcp",
        "--header",
        "X-Authorization: Basic <base64_encoded_cml_credentials>",
        "--header",
        "X-PyATS-Authorization: Basic <base64_encoded_device_credentials>"
      ]
    }
  }
}
```

Replace the placeholders with your actual values:

- `<server_host>`: The hostname or IP address where your HTTP server is running
- `<base64_encoded_cml_credentials>`: Base64-encoded `username:password` for CML
- `<base64_encoded_device_credentials>`: Base64-encoded `username:password` for device access

Example:

```json
{
  "mcpServers": {
    "Cisco Modeling Labs (CML)": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://192.168.10.210:8443/mcp",
        "--header",
        "X-Authorization: Basic <base64_encoded_cml_credentials>",
        "--header",
        "X-PyATS-Authorization: Basic <base64_encoded_device_credentials>"
      ]
    }
  }
}
```

**Note**: When using HTTPS with a self-signed certificate, you'll need to disable TLS certificate validation by adding an `env` section:

```json
{
  "mcpServers": {
    "Cisco Modeling Labs (CML)": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://192.168.10.210:8443/mcp",
        "--header",
        "X-Authorization: Basic <base64_encoded_cml_credentials>",
        "--header",
        "X-PyATS-Authorization: Basic <base64_encoded_device_credentials>"
      ],
      "env": {
        "NODE_TLS_REJECT_UNAUTHORIZED": "0"
      }
    }
  }
}
```

To encode your credentials in Base64:

**Linux/Mac:**

```sh
# For CML credentials
echo -n "username:password" | base64

# For device credentials  
echo -n "device_username:device_password" | base64

# For enable password (if needed)
echo -n "enable_password" | base64
```

**Windows (use WSL):**

```sh
wsl bash -c 'echo -n "username:password" | base64'
wsl bash -c 'echo -n "device_username:device_password" | base64'
wsl bash -c 'echo -n "enable_password" | base64'
```

Alternatively, you can use online Base64 encoders or PowerShell:

```powershell
[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("username:password"))
```

If you need to specify an enable password, add another header:

```json
"--header",
"X-PyATS-Enable: Basic <base64_encoded_enable_password>"
```

#### Docker with HTTP Transport

You can also run the server in HTTP mode using Docker:

```sh
docker run -d \
  --rm \
  --name cml-mcp \
  -p 9000:9000 \
  -e CML_URL=<URL_OF_CML_SERVER> \
  -e CML_MCP_TRANSPORT=http \
  xorrkaz/cml-mcp:latest
```

This exposes the HTTP server on port 9000, allowing external MCP clients to connect.

## Usage

The tools should show up automatically in your MCP client, and you can chat with the LLM to get it to invoke tools as needed.  For example,
the following sequence of prompts nicely shows off some of the server's capabilities:

- Create a new CML lab called "Joe's MCP Lab".
- Add two IOL nodes, a unmanaged switch, and an external connector to this lab.
- Connect the two IOL nodes to the unmanaged switch and the unmanaged switch to the external connector.
- Configure the routers so that their connected interfaces have IPs in the 192.0.2.0/24 subnet.  Configure OSPF on them.  Then start the lab and validate OSPF is working correctly.
- Add a box annotation around the two IOL nodes that indicates they speak OSPF.  Make it a green box.

And here is an obligatory demo GIF to show it working in Claude Desktop:

![Animated demonstration showing Claude Desktop creating a network topology in Cisco Modeling Labs through natural language commands. The sequence shows a user typing prompts to create a lab, add network devices including two IOL routers, an unmanaged switch, and an external connector, then configure OSPF routing between the devices. The interface displays both the chat conversation on the left and the resulting network diagram on the right, with nodes being added and connected in real-time as the AI processes each command.](img/cml_mcp.gif)

### System Prompt

If your LLM tool supports a system prompt, or you want to provide some richer initial context, here's a good example courtesy of Hank Preston:

>You are a network lab assistant specializing in supporting Cisco Modeling Labs (CML). You provide a natural language interface for many common lab activities such as:
>
>- Creating new lab
>- Adding nodes to a lab
>- Creating interfaces between nodes
>- Configuring nodes
>- Creating annotations
>
>You have access to tools to access the CML server.

## License

The MCP server portion of this project is licensed under the [BSD 2-Clause "Simplified" License](LICENSE).  However, it leverages the pydantic
schema typing code from CML itself, which is covered under a [proprietary Cisco license](src/cml_mcp/schemas/LICENSE).
