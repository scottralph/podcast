#! /usr/bin/bash
gcloud run deploy podcast --platform managed --region us-central1 --image gcr.io/scottralphorg-container/podcast --allow-unauthenticated --concurrency 80
d
