import torch
x = torch.rand(5, 3)
print(x)
print(f"CUDA: {torch.cuda.is_available()}")
