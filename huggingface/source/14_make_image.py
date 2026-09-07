# pip uninstall -y diffusers transformers huggingface-hub
# uv pip install --no-cache-dir -U huggingface-hub transformers diffusers
# pip install -U accelerate safetensors

from diffusers import StableDiffusionPipeline
import torch

model_id = "sd-legacy/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    dtype=torch.float32,
    safety_checker=None # NSFW 필터 제거(유해 이미지를 판단하는 필터)
).to("cuda")# mps

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]

image.save("image.png")