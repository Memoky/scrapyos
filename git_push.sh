#!/usr/bin/env bash
echo "正在添加文件..."
git add .
echo -n "正在提交备注...，请填写备注（可空）:"
if [  $1!='' ]  
then  
   msg=$1;  
else  
   msg='commit ';  
fi 
git commit -m "$msg"
echo "正在开始提交代码..."
git push github master
echo "代码提交成功，正在关闭..."