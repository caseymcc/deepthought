## Running ollama on amd

```
docker run -d --device /dev/kfd --device /dev/dri --env HIP_VISIBLE_DEVICES=1 -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm

docker exec -it ollama ollama pull {model}
```