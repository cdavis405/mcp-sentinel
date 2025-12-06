import asyncio
import os
import sys
import yaml
import json

sys.path.append(os.path.join(os.getcwd(), "src"))

from cml_driver.server import cml_client

def generate_interface_name(node_def, index):
    if node_def == "iosvl2":
        # Gi0/0, Gi0/1, Gi0/2, Gi0/3, Gi1/0 ...
        # Simplified: Gi0/0, Gi0/1, Gi0/2, Gi0/3
        return f"GigabitEthernet0/{index}"
    elif node_def == "csr1000v":
        # Gi1, Gi2, Gi3...
        return f"GigabitEthernet{index + 1}"
    elif node_def == "external_connector":
        return "port"
    else:
        # Fallback
        return f"eth{index}"

async def main():
    if len(sys.argv) < 2:
        print("Usage: python deploy_lab.py <path_to_yaml_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File not found {file_path}")
        sys.exit(1)

    print(f"Reading topology from {file_path}...")
    
    with open(file_path, 'r') as f:
        topology = yaml.safe_load(f)

    # Convert/Fix Topology
    print("Converting topology to CML format...")
    
    nodes_map = {n['id']: n for n in topology['nodes']}
    node_interfaces = {n['id']: [] for n in topology['nodes']} # List of assigned interface dicts
    
    # Process Links to assign interfaces
    new_links = []
    
    for link in topology['links']:
        l_id = link['id']
        n1_id = link['i1'] # In the yaml, i1 holds the node ID
        n2_id = link['i2'] # In the yaml, i2 holds the node ID
        
        # Determine interface for n1
        n1_def = nodes_map[n1_id]['node_definition']
        n1_idx = len(node_interfaces[n1_id])
        n1_intf_name = generate_interface_name(n1_def, n1_idx)
        n1_intf_id = f"{n1_id}-i{n1_idx}"
        
        # Add interface to node 1
        node_interfaces[n1_id].append({
            "id": n1_intf_id,
            "label": n1_intf_name,
            "type": "physical", # Assuming physical
            "node": n1_id
        })
        
        # Determine interface for n2
        n2_def = nodes_map[n2_id]['node_definition']
        n2_idx = len(node_interfaces[n2_id])
        n2_intf_name = generate_interface_name(n2_def, n2_idx)
        n2_intf_id = f"{n2_id}-i{n2_idx}"
        
        # Add interface to node 2
        node_interfaces[n2_id].append({
            "id": n2_intf_id,
            "label": n2_intf_name,
            "type": "physical",
            "node": n2_id
        })
        
        # Create new link object
        new_link = {
            "id": l_id,
            "label": link.get('id'), # Use ID as label if missing
            "n1": n1_id,
            "n2": n2_id,
            "i1": n1_intf_id,
            "i2": n2_intf_id,
            "conditioning": {}
        }
        new_links.append(new_link)

    # update nodes with interfaces
    for node in topology['nodes']:
        node['interfaces'] = node_interfaces[node['id']]
        # Ensure minimal configuration if missing
        if 'configuration' not in node and node['node_definition'] != "external_connector":
             node['configuration'] = ""

    # Replace links
    topology['links'] = new_links
    
    # Ensure lab has all required fields (version is required by schema)
    if 'lab' in topology:
         if 'version' not in topology['lab']:
             topology['lab']['version'] = "0.2.2" # Current common version

    print("Topology converted. Deploying...")
    # print(json.dumps(topology, indent=2)) 

    try:
        await cml_client.check_authentication()
        
        # Import to CML
        resp = await cml_client.post("/import", data=topology)
        
        print("\nDeployment successful!")
        print(f"Lab ID: {resp['id']}")
        
    except Exception as e:
        print(f"\nDeployment failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
