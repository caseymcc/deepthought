#!/bin/bash

forceStart=false
rebuild=false
while getopts "sr" flag
do
    case "${flag}" in
        s) forceStart=true;;
        r) rebuild=true;;
    esac
done


DOCKER_NAME="autogen_image"
CONTAINER_NAME="autogen_container"
PLATFORM=""
USER_NAME=$USER

if [ "$rebuild" = true ] || [ "$forceStart" = true ]; then

  running=$(docker container inspect -f '{{.State.Running}}' $CONTAINER_NAME 2>/dev/null)
  if [ "$running" == "true" ]; then
    echo "Stopping container"
    result=$(docker stop $CONTAINER_NAME)
  fi

  exists=$(docker ps -aq -f name=$CONTAINER_NAME)
  if [ "$exists" ]; then
    echo "Removing container"
    result=$(docker rm $CONTAINER_NAME)
  fi

  if [ "$rebuild" = true ]; then
    result=$(docker images -q $DOCKER_NAME )
    if [[ -n "$result" ]]; then
      "Deleting docker"
      result=$(docker rmi $DOCKER_NAME)
    fi
  fi
fi

result=$(docker images -q $DOCKER_NAME )
if [[ ! -n "$result" ]]; then
  echo "Building docker image"
  DOCKER_BUILDKIT=1 docker build \
    --build-arg USER_NAME=${USER} --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) \
    -t $DOCKER_NAME ./
fi

exists=$(docker ps -aq -f name=$CONTAINER_NAME)
if [ ! "$exists" ]; then
  echo "Creating docker"
  docker create -it --name $CONTAINER_NAME \
    --net=host \
    -v ${PWD}:/home/${USER}/$(basename ${PWD}) \
    -v ${PWD}/storage:/home/${USER}/$(basename ${PWD})/storage \
    $DOCKER_NAME
fi

running=$(docker container inspect -f '{{.State.Running}}' $CONTAINER_NAME 2>/dev/null)
if [ "$running" != "true" ]; then
  echo "Starting docker"
  result=$(docker start $CONTAINER_NAME)
fi

echo "Attaching to docker"
docker exec -it $CONTAINER_NAME bash

