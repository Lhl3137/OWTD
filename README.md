# OWTD Dataset

## 数据集简介
OWTD 数据集适用于各类算法研究与模型训练场景，本仓库仅提供数据集的下载方式与基础使用说明。

## 下载方式
### 百度网盘下载
- 链接：https://pan.baidu.com/s/1owF3QIne9EBppTYeTK_oPw?pwd=a5cy

# 油井图像分析系统

这是一个基于多模型融合的油井图像分析系统，可以自动检测油井位置并生成专业的分析报告。

## 功能特点

1. 使用YOLOv11模型检测图像中的油井位置和数量
2. 使用Qwen2.5-VL-72B-Instruct模型生成初步图像描述
3. 使用DeepSeek-V3模型生成专业的分析报告

## 环境要求

- Python 3.8+
- CUDA支持（推荐用于YOLOv11推理）

## 安装步骤

1. 克隆项目到本地
2. 安装依赖包：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 确保`best.pt`模型权重文件在项目根目录
2. 将要分析的图片放在`images`文件夹中
3. 运行程序：
```bash
python image_analyzer.py
```
4. 分析报告将保存在`analysis_report.txt`文件中

## 注意事项

- 请确保API密钥配置正确
- 确保图片格式为jpg或png
- 建议使用GPU进行推理以获得更好的性能 
