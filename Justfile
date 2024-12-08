build:
  docker buildx build --platform linux/amd64,linux/arm64 . --tag entec/helloworld:latest

push:
  docker push entec/helloworld:latest
