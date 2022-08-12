# BART API Demo

## Setup
```sh
# buld image
docker build -t bart-api-demo .

# run container in development mode
docker run -it --rm -v $(pwd):/app bart-api-demo:latest bash

# start API in development
docker run -it --rm -v $(pwd):/app --network="host" bart-api-demo:latest

# consume API (in another terminal)
curl -X GET localhost:80/

curl -X POST localhost:80/get-summary/ \
  -H "Content-Type: application/json" \
  --data-binary "@data/sample_request.json"
```

# Deployment

You should be able to deploy the image to any container hosting service (e.g. Azure Kubernetes Service, Azure Container Instance, etc.)

You may need to fiddle around with the port/host settings. During development, a workaround was to use the `--network="host"` flag when running `docker run`