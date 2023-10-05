# 论文写作思路 Medial-axis driven generative learning of synthetic 3D anatomical organs

## Abstract

keyword： Medial-axis、neural network
## 1. Introduction

（我都做了什么：

I. 准备数据集
    1. 首先是下载李建宁的数据，都是stl格式，然后手动剔除了不正确的shapes
    2. 把这些stl文件转换成ply格式，以用于point2skeleton项目生成骨架
    3. 生成的骨架是0_sphere.obj文件，至此，准备好了465个数据作数据集

II. 生成式网络训练
    1. 设计了一个全连接网络，可以接受骨架，输出一个肺动脉 
）

III. 表面重建
    1. 输出的肺动脉只是点云，还没有表面，采用了BPA算法做表面重建，有缝隙
    2. 用manifold技术完善表面，只留下一些holes
    <!-- 3. 再次manifold、或者用hole filling技术完善表面 -->
## 2. Related Work

### 2.1 Synthetic Data

### 2.2 