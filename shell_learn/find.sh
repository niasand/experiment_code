find ./test -name "abc.txt"

find ./test -iname "*.Php"  #忽略大小写


find ./test -maxdepth 2 -name "*.php" #显示目录查找深度

find ./test -not -name "*.php" #排除后缀为php的文件

find ./test -name 'abc*' ! -name '*.php' #查找所有以 abc 开头并且不含 .php 扩展名的文件


find -name '*.php' -o -name '*.txt'

./abc.txt
./subdir/how.php
./abc.php
./cool.php


find / -mtime +50 -mtime -100 #17. 查找某段时间范围内被修改过内容的文件

find / -size +50M -size -100M #查找大小在一定范围内的文件


find . -type f -exec ls -s {} \; | sort -n -r | head 5  #显示当前目录和子目录下最大的5个文件


find . -exec ls -ld {} \; #find 命令找到文件后，只能看到文件路径。如果想进一步查看文件信息，可以结合 ls 命令来实现。


find /tmp -type f -name "*.txt" -exec rm -f {} \; #会删除 tmp 目录下扩展名为 .txt 的文件。


find /tmp -type d -name "dirToRemove" -exec rm -r -f {} \; #我们同样可以删除目录，只要把 -type 后面的 f 改为 d ，并且在 rm 命令后面加上 -r 即可。



# refer link http://www.binarytides.com/linux-find-command-examples/