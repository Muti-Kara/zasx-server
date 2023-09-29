import subprocess
import yaml

with open('/opt/venvs.yml', 'r') as file:
    venvs = yaml.safe_load(file)['venvs']

for venv in venvs:
    name = venv['name']
    packages = venv.get('packages', []) + ['jupyter']

    print(f"At {name}")

    subprocess.run(['python', '-m', 'venv', '--system-site-packages', f'/opt/venvs/{name}'])

    subprocess.run([f"/opt/venvs/{name}/bin/python", "-m", 'pip', 'install', '-U'] + packages)

    subprocess.run([f"/opt/venvs/{name}/bin/python", "-m", "ipykernel", "install", "--name", name])

print("Virtual environments created successfully.")
