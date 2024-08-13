import requests

# Your DigitalOcean API token
API_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxx'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_TOKEN}'
}

# Function to list all droplets
def list_droplets():
    url = 'https://api.digitalocean.com/v2/droplets'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        droplets = response.json()['droplets']
        for idx, droplet in enumerate(droplets):
            public_ip = private_ip = 'None'
            for network in droplet['networks']['v4']:
                if network['type'] == 'public':
                    public_ip = network['ip_address']
                elif network['type'] == 'private':
                    private_ip = network['ip_address']
            region = droplet['region']['name']
            print(f"{idx + 1}. ID: {droplet['id']}, Name: {droplet['name']}, Status: {droplet['status']}, Public IP: {public_ip}, Region: {region}")
        return droplets
    else:
        print(f"Failed to list droplets: {response.status_code} {response.text}")
        return None

# Function to delete a droplet by ID
def delete_droplet(droplet_id):
    url = f'https://api.digitalocean.com/v2/droplets/{droplet_id}'
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Droplet {droplet_id} deleted successfully.")
    else:
        print(f"Failed to delete droplet {droplet_id}: {response.status_code} {response.text}")

# List all droplets
droplets = list_droplets()

# If there are droplets, prompt the user to select one for deletion
if droplets:
    try:
        selection = int(input("Enter the number of the droplet you want to delete: ")) - 1
        if 0 <= selection < len(droplets):
            droplet_id_to_delete = droplets[selection]['id']
            confirmation = input(f"Are you sure you want to delete droplet {droplet_id_to_delete}? (y/n): ")
            if confirmation.lower() == 'y':
                delete_droplet(droplet_id_to_delete)
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")
else:
    print("No droplets found.")
