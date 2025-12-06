import asyncio
import os
import json
import sys
# sys.path.append(os.path.join(os.getcwd(), "src")) # uv should handle this if running correctly, or we can keep it
from cml_driver.settings import settings
from cml_driver.server import get_all_labs, cml_client

async def main():
    try:
        # CMLClient usually does auto-auth on first request or we can call check_authentication
        await cml_client.check_authentication()

        labs = await get_all_labs()
        print(f"Found {len(labs)} labs:")
        for lab_id in labs:
            try:
                lab = await cml_client.get(f"/labs/{lab_id}")
                print(f"Lab ID: {lab_id}")
                # Print full lab dict to debug
                print(json.dumps(lab, indent=2))
                
                title = lab.get('title') or lab.get('lab_title') or "Unknown"
                print(f"- {title} (ID: {lab_id})")
            except Exception as e:
                print(f"- Error fetching details for {lab_id}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
