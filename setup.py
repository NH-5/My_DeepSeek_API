from cx_Freeze import setup, Executable

# 定义可执行文件
executables = [
    Executable(
        script="deepseek.py",        # 要打包的脚本
        #base="Win32GUI",              # 隐藏控制台窗口（适用于 GUI 程序）
        target_name="deepseek.exe",      # 生成的 EXE 文件名
        #icon="myicon.ico",            # EXE 文件的图标
        #shortcut_name="My Application",  # 快捷方式名称
        #shortcut_dir="ProgramMenuFolder" # 快捷方式目录
    )
]

build_options = {
    "packages": ["openai","deepseek_R1","deepseek_V3"],  # 需要包含的第三方库
    #"include_files": ["deepseek_R1.py","deepseek_V3.py"],  # 需要包含的数据文件或文件夹
    #"excludes": ["tkinter"],  # 排除不需要的模块
}

# 调用 setup 函数
setup(
    name="deepseek",                     # 应用程序名称
    version="1.0",                    # 版本号
    description="my own deepseek app with api",  # 描述
    options={"build_exe": build_options},
    executables=executables           # 可执行文件配置
)