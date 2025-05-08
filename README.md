# Flask App DevSecOps

This repository contains a secure, login-based Flask application deployed using GitHub Actions, Helm, Argo CD, and Vault, following DevSecOps best practices.

## Features
- ��� Secrets management via Vault
- ��� Integrated SAST, SCA, and DAST tools
- ��� Packaged as a Docker image
- ��� CI/CD with GitHub Actions
- ��� GitOps deployment with Argo CD

## Folder Structure
```
flask-app-devsecops/
��├── flask-app/               # Flask app & Dockerfile
├── flask-app-helm/          # Helm chart
├── environments/            # Dev & stage values
├── argocd-dev.yaml          # Argo CD app for dev
├── argocd-stage.yaml        # Argo CD app for stage
```

## Usage
1. Build and push Docker image
2. Sync app in Argo CD
3. Vault injects runtime secrets
# test credential cache
