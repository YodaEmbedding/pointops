# pointops

`pointops` is a collection autograd-compatible point cloud operations for PyTorch. The operations are implemented in C++ and CUDA.

Original source:

- https://github.com/hszhao/PointWeb/tree/master/lib/pointops
- https://github.com/CVMI-Lab/PAConv/tree/main/scene_seg/lib/pointops

The only modification applied is to remove the obsolete THC import:

```bash
sed -i 's:^\([^/].*\bTHC.*\)$://\1:' pointops/src/**/*.cpp
```

Copyright rests with the original authors.
