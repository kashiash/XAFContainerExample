import paramiko

# Dane logowania do serwera
hostname = "192.168.x.x"
username = "username"
password = "password"

# Dane logowania do Docker Hub
docker_username = "docker_username"
docker_password = "docker_password"

# Komendy do wykonania na serwerze
commands = [
    "cd /home/dockerrunner",
    "echo {password} | sudo -S docker-compose -f /home/dockerrunner/docker-compose.yaml down",
    f"echo {docker_password} | docker login -u {docker_username} --password-stdin",
    "echo {password} | sudo -S docker-compose -f /home/dockerrunner/docker-compose.yaml pull",
    "echo {password} | sudo -S docker-compose -f /home/dockerrunner/docker-compose.yaml up -d"
]

def execute_commands(commands, client):
    for command in commands:
        stdin, stdout, stderr = client.exec_command(command.format(password=password))
        print(stdout.read().decode())
        print(stderr.read().decode())

def main():
    # Połączenie SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)

    # Wykonanie komend
    execute_commands(commands, client)

    # Zamknięcie połączenia
    client.close()

if __name__ == "__main__":
    main()