provider "aws" {
  region = "ap-south-1"
}

resource "aws_security_group" "cloudforge_sg" {
  name = "cloudforge-sg"

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 9090
    to_port = 9090
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 3000
    to_port = 3000
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "cloudforge_instance" {
  ami = "ami-05d2d839d4f73aafb"
  instance_type = "t2.micro"
  key_name = "cloudforge_key"

  vpc_security_group_ids = [aws_security_group.cloudforge_sg.id]

  tags = {
    Name = "CloudForge-Instance"
  }
}

output "instance_ip" {
  value = aws_instance.cloudforge_instance.public_ip
}