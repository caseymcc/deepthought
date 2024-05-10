
## Starting with nvidia gpu
```
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker exec -it ollama ollama run mixtral
```

## Starting with rocm (AMD)
```
docker run -d --env CUDA_VISIBLE_DEVICES=0 \
    --device=/dev/kfd --device=/dev/dri \
    --security-opt seccomp=unconfined \
    --group-add video \
    --group-add render \
    -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker exec -it ollama ollama run llama2
```