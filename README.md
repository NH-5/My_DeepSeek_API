# DeepSeek API 客户端

使用DeepSeek API在本地端使用DeepSeek模型，支持Windows、macOS和Linux平台。

## 特点

- 支持DeepSeek-V3和DeepSeek-R1模型
- 流式输出回复
- 简单的命令行界面
- 跨平台支持

## 下载与安装

### 预编译版本

访问 [GitHub Releases](https://github.com/NH-5/My_DeepSeek_API.git/releases) 下载最新版本的预编译可执行文件。

### 从源代码构建

1. 克隆仓库：
   ```
   git clone https://github.com/NH-5/My_DeepSeek_API.git
   cd My_DeepSeek_API
   ```

2. 安装依赖：
   ```
   pip install cx_Freeze openai
   ```

3. 构建可执行文件：
   ```
   python setup.py build
   ```

4. 构建完成后，可执行文件将位于 `build/exe.系统平台-架构/` 目录下。

## 使用方法

1. 运行可执行文件
2. 输入您的DeepSeek API密钥
3. 选择要使用的模型：
   - 1: DeepSeek-V3 (通用对话模型)
   - 2: DeepSeek-R1 (推理增强模型)
4. 输入您的问题，程序将以流式方式显示回答
5. 如需退出当前模型对话，输入 `exit`
6. 如需完全退出程序，选择选项 `3`

## API密钥获取

需要用户在[DeepSeek官方网站](https://platform.deepseek.com/)申请API密钥。

## 温度设置参考

代码中支持调整temperature参数，以下是官方建议：
- 代码生成/数学解题: 0.0
- 数据抽取/分析: 1.0
- 通用对话: 1.3
- 翻译: 1.3
- 创意类写作/诗歌创作: 1.5

## 开发者说明

可通过修改`deepseek_R1.py`和`deepseek_V3.py`中的参数来自定义模型行为。