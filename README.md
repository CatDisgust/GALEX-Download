# GALEX 数据下载器

## 项目简介
GALEX数据下载器是一个Python项目，用于自动从AWS S3桶下载GALEX（Galaxy Evolution Explorer）数据集。此项目旨在帮助研究人员和数据科学家方便地获取天文数据，以便进行进一步的分析和研究。

## 功能
- 从指定的AWS S3桶下载GALEX数据。
- 支持下载特定文件或整个数据集。
- 自动保存下载的数据到本地指定路径。

## 安装
在开始之前，确保您的系统已经安装了Python和pip。然后，使用以下命令安装必要的依赖：

```bash
pip install -r requirements.txt
```

## 配置
- 在 config.py 中设置AWS S3桶的信息，包括桶名、路径和区域。
- 在 utils.py 中设置AWS安全凭证
- 设置本地保存路径