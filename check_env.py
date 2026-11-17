"""Confirm the environment works: print versions and run one tensor operation."""
import sys

import numpy as np
import torch

print(f"Python  {sys.version.split()[0]}")
print(f"NumPy   {np.__version__}")
print(f"PyTorch {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

x = torch.tensor([1.0, 2.0, 3.0])
print(f"x     = {x}")
print(f"x * 2 = {x * 2}")