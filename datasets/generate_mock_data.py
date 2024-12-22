import numpy as np
import h5py
import os

# 创建输出目录
output_dir = 'data/processed'
os.makedirs(output_dir, exist_ok=True)

# 生成模拟 .npz 数据
npz_path = os.path.join(output_dir, 'mock_data.npz')
data = np.random.rand(100, 10)  # 模拟 100 个样本，每个有 10 个特征
labels = np.random.randint(0, 2, size=(100,))  # 模拟二分类标签
np.savez(npz_path, data=data, labels=labels)
print(f"模拟 .npz 数据生成完毕，保存至: {npz_path}")

# 生成模拟 .hdf5 数据
hdf5_path = os.path.join(output_dir, 'mock_data.hdf5')
with h5py.File(hdf5_path, 'w') as f:
    f.create_dataset('data', data=data)
    f.create_dataset('labels', data=labels)
print(f"模拟 .hdf5 数据生成完毕，保存至: {hdf5_path}")
