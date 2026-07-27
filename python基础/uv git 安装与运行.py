"""
1、uv安装
1.1官网：https://docs.astral.sh/uv/getting-started/installation/#standalone-installer
1.2以管理员身份打开PowerShell
点击开始按钮或按键盘上的Windows键在搜索框中输入 "PowerShell"在搜索结果中右键单击 "Windows PowerShell"选择 "以管理员身份运行"
1.3按官网提示安装，并通过重启后的PowerShell输入 uv –version，验证是否安装成功；
1.4选择相应的版本python编译器就会配置相应的虚拟环境
1.5常用操作及命令
项目初始化与环境管理
uv init my_project 在当前目录创建新的 Python 项目
uv venv .venv 创建虚拟环境
uv venv --python 3.12 指定 Python 版本创建虚拟环境
uv python pin 3.12 锁定项目使用的 Python 版本

包管理（核心功能）
uv add <package> 安装包并添加到 pyproject.toml
uv add <package>==版本号 安装指定版本
uv add <package> --dev 安装为开发依赖
uv sync 同步 pyproject.toml 中的依赖到虚拟环境
uv remove <package> 移除包
uv lock 生成/更新 uv.lock 锁定文件

替代 pip 的命令
uv pip install <package> 安装包（不写入 pyproject.toml）
uv pip install -r requirements.txt 从 requirements.txt 安装
uv pip uninstall <package> 卸载包
uv pip freeze 列出已安装的包
uv pip list 列出已安装的包及其版本
uv pip show <package> 显示包详细信息
uv pip check   检查依赖冲突
uv pip compile 从 pyproject.toml 生成 requirements.txt

# 1. 创建新项目
uv init my_project
cd my_project

# 2. 创建虚拟环境
uv venv

# 3. 激活虚拟环境
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows

# 4. 安装依赖
uv add fastapi uvicorn

# 5. 运行项目
uv run uvicorn main:app --reload

# 6. 安装开发依赖
uv add pytest httpx --dev

# 7. 同步依赖（确保环境一致）
uv sync

常用命令速查表
uv init          # 初始化项目
uv venv          # 创建虚拟环境
uv add           # 添加依赖
uv sync          # 同步依赖
uv lock          # 锁定版本
uv remove        # 移除依赖
uv run           # 运行命令
uv build         # 构建项目
uv publish       # 发布到 PyPI
uv pip install   # 传统 pip 风格安装
uv tree          # 查看依赖树
uv cache clean   # 清理缓存

管理多个版本
uv python list                  # 列出可用的 Python 版本
uv python install 3.11 3.12     # 安装多个 Python 版本
uv venv --python 3.11           # 指定 Python 版本创建环境

加速安装
# 使用镜像源（中国大陆）
uv add flask --index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 或设置环境变量
export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

从requirements.txt 迁移
# 自动检测并安装 requirements.txt 中的依赖
uv add $(cat requirements.txt)

# 或直接使用 pip 兼容模式
uv pip install -r requirements.txt

版本查看与帮助
uv --version         # 查看版本
uv --help            # 查看帮助
uv <command> --help  # 查看具体命令的帮助

2、git
2.1官网：https://git-scm.com/install/windows
2.2加速：通过window应用商店下载Watt Toolkit,在列表选择git加速；
2.3在 Git 安装过程中，当进行到 Choosing the default editor used by Git 这一步时，在编辑器选择下拉框中，选择
"Select other editor as Git's default editor" 或类似的选项。
2.4在 PyCharm 中配置 Git
安装完成后，还需要在 PyCharm 内部配置 Git：
（1）打开 PyCharm → File → Settings（或 Ctrl+Alt+S）
（2）进入 Version Control → Git
（3）在 Path to Git executable 中选择 Git 的安装路径（如 C:\Program Files\Git\bin\git.exe）
（4）点击 Test 按钮，如果显示 Git 版本号，则配置成功
2.5验证设置
在cmd窗口中输入git config --global core.editor，如果返回你设置的 PyCharm 路径，说明设置成功。
2.6git常见命令
git clone <git地址>；复制git上其他的仓库 在所在文件夹，右键选择bash；
初始化仓库：git init

添加文件到暂存区：git add -A
把暂存区的文件提交到仓库：git commit -m "提交信息"
查看提交的历史记录：git log --stat

工作区回滚：git checkout <filename>
撤销最后一次提交：git reset HEAD^1

以当前分支为基础新建分支：git checkout -b <branchname>
列举所有的分支：git branch
单纯地切换到某个分支：git checkout <branchname>
删掉特定的分支：git branch -D <branchname>
合并分支：git merge <branchname>

3、为pycharm设置版本控制
通过 Token 登录（推荐）
打开 PyCharm → File → Settings（Windows）或 PyCharm → Preferences（Mac）
进入 Version Control → GitHub
点击 Add account → Log in with Token
在 GitHub 网站上生成 Token（路径：Settings → Developer settings → Personal access tokens），勾选 repo 和 gist 权限
将 Token 粘贴到 PyCharm 中，点击 Add Account







"""