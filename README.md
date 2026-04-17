<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body>

  <h1>🚀 CloudForge – Automated Cloud Infrastructure Platform</h1>

  <p>
    <strong>CloudForge</strong> is a backend-driven cloud automation platform that provisions and manages infrastructure on AWS using APIs. Built with FastAPI and Terraform, it allows users to create and destroy EC2 environments, deploy applications, and monitor system health in real-time. The project integrates CI/CD using GitHub Actions and includes observability with Prometheus and Grafana, demonstrating real-world DevOps workflows and infrastructure automation.
  </p>

  <h2>🚀 Project Highlights</h2>
  <ul>
    <li>⚡ API-driven infrastructure provisioning using FastAPI</li>
    <li>☁️ Automated EC2 creation and destruction via Terraform</li>
    <li>🔐 Secure SSH-based deployment using Paramiko</li>
    <li>🔄 CI/CD pipeline via GitHub Actions</li>
    <li>🧠 System status endpoint with real-time instance tracking</li>
    <li>📈 Monitoring with Prometheus & Grafana</li>
    <li>🖥️ Production-ready backend managed using systemd</li>
    <li>🌍 Hosted on AWS EC2 (Ubuntu)</li>
  </ul>

  <h2>🛠️ Technologies Used</h2>
  <ul>
    <li>Python & FastAPI (Backend)</li>
    <li>Terraform (Infrastructure as Code)</li>
    <li>AWS EC2 (Ubuntu)</li>
    <li>Paramiko (SSH Automation)</li>
    <li>Prometheus + Grafana</li>
    <li>GitHub Actions (CI/CD)</li>
    <li>systemd (Process Management)</li>
  </ul>

  <h2>📊 Architecture Overview</h2>
  <ul>
    <li>FastAPI backend exposes endpoints like <code>/create-environment</code>, <code>/destroy-environment</code>, and <code>/status</code></li>
    <li>Backend triggers Terraform to provision AWS EC2 instances</li>
    <li>Paramiko is used to SSH into instances and deploy applications</li>
    <li>Prometheus collects system metrics from running services</li>
    <li>Grafana visualizes CPU, memory, and uptime metrics</li>
    <li>GitHub Actions automates deployment to EC2 on every push</li>
  </ul>

  <h2>📸 Project Screenshots</h2>
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/1.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/2.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/3.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/4.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/5.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/6.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/7.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/8.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/9.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/10.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/11.PNG" width="600"/>
  <br />
  <img src="https://github.com/Birarvindersingh/cloudforge/blob/main/screenshots/12.PNG" width="600"/>

  <h2>📈 Monitoring with Grafana + Prometheus</h2>
  <ul>
    <li>Prometheus collects metrics from backend services</li>
    <li>Grafana visualizes system performance (CPU, memory, uptime)</li>
    <li>Dashboards provide real-time monitoring of deployed environments</li>
  </ul>

  <h2>🛡️ CI/CD Pipeline</h2>
  <ul>
    <li>GitHub Actions triggers deployment on every push to main branch</li>
    <li>Automatically connects to EC2 via SSH</li>
    <li>Pulls latest code, installs dependencies, and restarts backend</li>
    <li>Systemd ensures the FastAPI service runs continuously</li>
  </ul>

  <h2>✅ Conclusion</h2>
  <p>This project demonstrates practical DevOps and cloud engineering skills by combining infrastructure automation, backend development, CI/CD pipelines, and monitoring into a production-ready system.</p>

</body>
</html>
