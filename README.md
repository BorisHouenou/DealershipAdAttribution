# DealershipAdAttribution
Solution Architecture for Cloud‑Native Dealership Attribution Platform

# Dealership Attribution Platform

End-to-end, cloud-native attribution solution for automotive dealerships.

## Modules

- **terraform/** — Infrastructure as Code (AWS).
- **lambda/** — Serverless data ingestion (Facebook Ads, CRM webhooks).
- **etl/** — AWS Glue ETL jobs for data transformation.
- **modeling/** — Bayesian Marketing Mix Model implementation.
- **container/** — Flask API for attribution queries.
- **.github/** — CI/CD workflows.

## Setup

1. Configure AWS credentials.
2. `cd terraform && terraform init && terraform apply`.
3. Deploy Lambdas: `make deploy-lambdas`.
4. Set up Glue jobs: upload scripts from `etl/` to AWS Glue.
5. Build and push Docker: `docker build -t attribution-api container/`.
6. Deploy API to ECS/Fargate.
7. Run modeling notebooks or integrate via API.
