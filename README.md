# Pulumi AWS S3 Automation 🚀

This repository contains a Python script that uses [Pulumi](https://www.pulumi.com/) to automate the creation and management of an AWS S3 bucket. The script demonstrates Infrastructure as Code (IaC) principles, making it easy to provision and manage cloud resources programmatically.

## Features
- Creates an AWS S3 bucket with:
  - **Private Access Control** for enhanced security.
  - **Tags** for better resource organization (`Environment: Dev`, `Team: SRE`).
- Exports the bucket name for further use in other applications or workflows.

## Prerequisites
- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/) installed.
- AWS credentials configured locally (e.g., via `aws configure`).
- Python 3.x installed with `pip`.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Pulumi-AWS-S3-Automation.git
   cd Pulumi-AWS-S3-Automation
