from PIL import Image

img = Image.open("practice.png").convert("RGB")

display(img)

import torch


def run(img, pretrained):
    model = torch.hub.load(
        "bryandlee/animegan2-pytorch:main", "generator", pretrained=pretrained
    )
    face2paint = torch.hub.load(
        "bryandlee/animegan2-pytorch:main", "face2paint", size=512
    )
    out = face2paint(model, img)
    display(out)

run(img, "celeba_distill")
run(img, "face_paint_512_v1")
run(img, "face_paint_512_v2")
run(img, "paprika")
