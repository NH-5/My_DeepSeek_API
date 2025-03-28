from cx_Freeze import setup, Executable
import sys
import os

# 确定基础设置
base = None
target_name = "deepseek"

# 根据操作系统设置特定参数
if sys.platform == "win32":
    base = "Console"  # 使用控制台应用
    target_name = "deepseek.exe"

# 定义可执行文件
executables = [
    Executable(
        script="deepseek.py",        # 要打包的脚本
        base=base,                   # 根据平台设置
        target_name=target_name,     # 生成的可执行文件名
    )
]

# 包含依赖文件
include_files = [
    "deepseek_R1.py", 
    "deepseek_V3.py"
]

# 构建选项
build_options = {
    "packages": ["openai"],
    "include_files": include_files,
    "include_msvcr": True,  # 在Windows上打包MSVC运行时
}

# 调用 setup 函数
setup(
    name="deepseek",
    version="1.0",
    description="DeepSeek API 客户端应用",
    options={"build_exe": build_options},
    executables=executables
)