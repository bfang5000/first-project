# first-project
第一个python项目


# 提交代码到远程仓库
# 1. 检查当前状态（确认文件是否已暂存）
git status

# 2. 添加文件到暂存区（若尚未暂存）
git add basicdatatype.py
# 或添加全部修改
git add .

# 3. 执行提交（带提交信息）
git commit -m "feat: add basicdatatype module
>
> - 新增基本数据类型演示代码
> - 包含字符串、数字等类型示例"

# 4. 推送代码到远程仓库
git push origin 20250329  # 根据你的上下文显示当前分支是 20250329

# 5. 再合并到主分支
# 1）. 切换到主分支
git checkout main  # 或 git checkout master（根据你的主分支名称）

# 2）. 拉取最新代码（确保主分支最新）
git pull origin main

# 3）. 执行合并（将 20250329 分支合并到主分支）
git merge 20250329

# 如果有冲突先手动解决冲突，再执行git add. 
# git commit -m "feat: resolve conflicts"
# 4）. 推送合并后的主分支
git push origin main



注意事项：

-m 参数后的消息格式：
首行简明标题（建议遵循 Conventional Commits 规范）
空行后写详细说明（使用 > 符号换行）
如果未配置用户信息需先执行：
bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
提交时若忘记 -m 参数会自动打开编辑器（即你遇到的 COMMIT_EDITMSG 文件），此时：
按 i 进入编辑模式
输入提交信息
按 Esc 后输入 :wq 保存退出