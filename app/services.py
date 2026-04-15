import subprocess
import paramiko
import time

KEY_PATH = "/home/ubuntu/cloudforge_key.pem"
INSTANCE_IP = "SERVER_IP"

def create_env():
    try:
        subprocess.run(
            ["terraform", "init"],
            cwd="terraform",
            check=True
        )

        subprocess.run(
            ["terraform", "apply", "-auto-approve"],
            cwd="terraform",
            check=True
        )

        result = subprocess.check_output(
            ["terraform", "output", "-raw", "instance_ip"],
            cwd="terraform"
        )

        ip = result.decode().strip()

        deploy_app(ip)

        return {
            "status": "success",
            "message": "Environment created & app deployed",
            "url": f"http://{ip}"
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def deploy_app(ip):
    time.sleep(60)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=ip, username="ubuntu", key_filename=KEY_PATH)

    commands = [
        "sudo apt update -y",
        "sudo apt install docker.io -y",
        "sudo systemctl start docker",
        "sudo docker run -d -p 80:80 nginx",
        "sudo docker run -d -p 9100:9100 prom/node-exporter",
        "sudo docker run -d -p 9090:9090 prom/prometheus",
        "sudo docker run -d -p 3000:3000 grafana/grafana"
    ]

    for cmd in commands:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
        print(stderr.read().decode())

    ssh.close()

def stop_env():
    return run_ssh_command("sudo docker stop $(sudo docker ps -q)")

def start_env():
    return run_ssh_command("sudo docker start $(sudo docker ps -aq)")

def restart_env():
    return run_ssh_command("sudo docker restart $(sudo docker ps -q)")

def run_ssh_command(command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=INSTANCE_IP,
            username="ubuntu",
            key_filename=KEY_PATH
        )

        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        ssh.close()

        return {
            "status": "success",
            "output": output,
            "error": error
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def destroy_env():
    try:
        subprocess.run(
            ["terraform", "destroy", "-auto-approve"],
            cwd="terraform",
            check=True
        )

        return {
            "status": "success",
            "message": "Infrastructure destroyed"
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def get_status():
    return {
        "status": "running",
        "instances": 1,
        "health": "ok"
    }