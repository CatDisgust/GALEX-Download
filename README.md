# GALEX下载项目

## 项目简介
这个项目提供了从GALEX（银河演化探测器）数据集下载数据的工具。它使用了Astroquery库来查询和下载特定天空区域内的天文数据。

## 安装步骤
要安装必要的依赖项，请在项目根目录下运行以下命令：
```shell
    pip install -r requirements.txt
   ```



## 使用方法
使用以下命令格式运行脚本：
    ```shell 
    python download_galex.py <coordinate> <radius> <download_path>
    ```

- `<coordinate>`: 搜索的天空坐标（赤经和赤纬），例如 "10.6840 -41.2690"。
- `<radius>`: 搜索半径，单位为度，例如 "0.1 deg"。
- `<download_path>`: 数据下载的目标文件夹路径。

例如，运行以下命令来下载数据：
```shell
python download_galex.py "10.6840 -41.2690" "0.1 deg" "./galex_data"
```


## 注意事项
- 确保在运行脚本之前已安装所有依赖。
- 根据网络状况和数据量，下载过程可能需要一定的时间。

## 已知问题
（在这里列出项目的任何已知问题或限制。如果没有已知问题，可以省略此部分。）

## 许可证
（如果适用，添加许可证信息。）

## 联系方式
（提供项目维护者的联系方式，如电子邮件地址。）# GALEX-Download
# GALEX-Download
