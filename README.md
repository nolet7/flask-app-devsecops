# Flask App DevSecOps

This repository contains a secure, login-based Flask application deployed using GitHub Actions, Helm, Argo CD, and Vault, following DevSecOps best practices.

## Features
- ³Ší Secrets management via Vault
- ´í Integrated SAST, SCA, and DAST tools
- ·ªí Packaged as a Docker image
- ³¦í CI/CD with GitHub Actions
- º€í GitOps deployment with Argo CD

## Folder Structure
```
flask-app-devsecops/
³Šâ”œâ”€â”€ flask-app/               # Flask app & Dockerfile
â”œâ”€â”€ flask-app-helm/          # Helm chart
â”œâ”€â”€ environments/            # Dev & stage values
â”œâ”€â”€ argocd-dev.yaml          # Argo CD app for dev
â”œâ”€â”€ argocd-stage.yaml        # Argo CD app for stage
```

## Usage
1. Build and push Docker image
2. Sync app in Argo CD
3. Vault injects runtime secrets
# test credential cache
