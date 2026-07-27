"""
1、uv安装
1.1官网：https://docs.astral.sh/uv/getting-started/installation/#standalone-installer
1.2以管理员身份打开PowerShell
点击开始按钮或按键盘上的Windows键在搜索框中输入 "PowerShell"在搜索结果中右键单击 "Windows PowerShell"选择 "以管理员身份运行"
1.3按官网提示安装，并通过重启后的PowerShell输入 uv –version，验证是否安装成功；


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