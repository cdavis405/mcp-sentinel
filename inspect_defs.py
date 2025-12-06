import asyncio
import os
import sys
import json

sys.path.append(os.path.join(os.getcwd(), "src"))

from cml_driver.server import cml_client
from cml_driver.types import SuperSimplifiedNodeDefinitionResponse

async def main():
    try:
        await cml_client.check_authentication()
        
        # Get list of definitions directly
        node_definitions = await cml_client.get("/simplified_node_definitions")
        defs = [SuperSimplifiedNodeDefinitionResponse(**nd) for nd in node_definitions]
        print(f"Found {len(defs)} definitions")
        
        target_defs = ["external_connector"]
        
        for d in defs:
            if d.id in target_defs:
                print(f"\n--- {d.id} ---")
                details = await cml_client.get(f"/node_definitions/{d.id}", params={"json": True})
                print(f"Keys: {list(details.keys())}")
                if 'device' in details:
                    print("Device:", json.dumps(details['device'], indent=2))
                if 'sim' in details:
                    print("Sim:", json.dumps(details['sim'], indent=2))



    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
