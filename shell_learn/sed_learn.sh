# -n表示取消默认输出,p表示打印行
sed -n 'p' /etc/passwd
# 只打印第三行
sed -n '3p' /etc/passwd
# 打印1，3行
sed -n '1,3p' /etc/passwd


#-i会修改源文件,但是可以同时使用bak备份
sed -ibak 's/Ian/IAN/' source.txt 

# -l会显示隐藏字符比如'\t', = 可以显示行号
sed -l = source.txt
# y或翻译你要转换的字符,这里I会转化成i，B转换成b
sed 'y/IB/ib/' source.txt |head -1


awk -Fs '/pattern/ {action}' input-file
#or
awk -Fs '{action}' intput-file
# -F表示设置分隔符,不指定就是默认为空字符

# 用:分割，查找匹配mail的行并且打印冒号分割后的第一部分
awk -F: '/mail/ {print $1}' /etc/passwd
# _mailman
# _clamav
# _amavisd


# awk 的关联数组中item[101]和item["101"]意义一样
awk 'BEGIN { item[101]="Github"; print item["101"]}'
Github
# 可以用in检验是否包含本项
awk 'BEGIN { item[101]="a"; if ( 101 in item ) print "Has 101"}'
Has 101
# 还可以使用for循环读取列表
cat array-for-loop.awk
BEGIN {
    item[101]="Github";
    item[21]="Google";
    for (x in item)
        print item[x];
}
awk -f array-for-loop.awk
Github
Google
# 多维数组, delete可以删除元素.PS item[2,1]这样的格式有问题
# 因为会被翻译成2#2("2\0342"),假设要设置分隔符可以使用SUBSEP=",";
awk 'BEGIN { item["1,1"]="Github"; item["1,2"]="Google"; \
item["2,1"]="Whim"; delete item["2,1"];
for (x in item)
print "Index",x,"contains",item[x];}'
Index 1,1 contains Github
Index 1,2 contains Google




# 这里需要gnu awk了 使用了asort排序
$cat asort.awk 
BEGIN {
 item[101]="Github";
 item[22]="Whim";
 item[50]="Google";
 print "------Before asort------"
 for (x in item)
     print "Index",x,"contains",item[x];
 total = asort(item);
 print "------After asort------"
 for (x in item)
     print "Index",x,"contains",item[x];
}

gawk -f asort.awk
------Before asort------
Index 22 contains Whim
Index 50 contains Google
Index 101 contains Github
------After asort------
Index 1 contains Github
Index 2 contains Google
Index 3 contains Whim
# 大家请注意上面的例子,排序后已经忘记了原来item的index位置
# 而asorti可以帮助你记录这个位置
cat asorti.awk
BEGIN {
 item[101]="Github";
 item[22]="Whim";
 item[50]="Google";
 print "----- Function: asort -----"
 total = asort(item,itemdesc);
 for (i=1; i<= total; i++)
    print "Index",i,"contains",itemdesc[i];
 print "----- Function: asorti -----"
 total = asorti(item,itemabbr);
 for (i=1; i<= total; i++)
     print "Index",i,"contains",itemabbr[i];
}
gawk -f asorti.awk
----- Function: asort -----
Index 1 contains Github
Index 2 contains Google
Index 3 contains Whim
----- Function: asorti -----
Index 1 contains 101
Index 2 contains 22
Index 3 contains 50



#格式化打印

# \n是换行
awk 'BEGIN { printf "Line 1\nLine 2\n" }'
Line 1
Line 2
# \t是tab
awk 'BEGIN \
{ printf "Field 1\t\tField 2\tField 3\tField 4\n" }'
Field 1		Field 2	Field 3	Field 4
# \v是垂直tab
awk 'BEGIN \
{ printf "Field 1\vField 2\vField 3\vField 4\n" }'
Field 1
    Field 2
       Field 3
	  Field 4
# %s字符串; %c单个字符; %d数字; %f浮点数......
cat printf-width.awk 
BEGIN {
FS=","
printf "%3s\t%10s\t%10s\t%5s\t%3s\n",
    "Num","Description","Type","Price","Qty"
printf "-----------------------------------------------------\n"
}
{
    printf "%3d\t%10s\t%10s\t%g\t%d\n", $1,$2,$3,$4,$5
}




# int - 将数字转换成整形, 类似的函数还有sqrt, sin, cos...
awk 'BEGIN {print int(4.1);print int(-6.22);print int(strings)}'
4
-6
0
# rand - 随机0-1的数字; srand -初始化随机数的初始值
cat srand.awk 
BEGIN {
    srand(5);
    count=0;
    max=30;
    while (count < 5) {
        # 随机数范围为5-30
        rnd = int(rand() * max);
        print rnd;
        count++;
    }
}
# 使用osx的awk随机范围不对
gawk -f srand.awk
19
9
21
8
13
# index - 所查字符在字符串中的位置,没找到会返回0
awk 'BEGIN{str="This is a test"; print index(str, "a"); print index(str, "y")}'
9
0
# length - 字符串的长度
awk -F, '{print length($0)}' source.txt
23
24
21
22
26
25
25
# split - 分片 PS:使用awk分片的顺序有问题;
# split第一个参数是要分割的内容,第二个是分割后的结果保存的数组,第三个是使用的分隔符
echo "101 arg1:arg2:arg3"|gawk '{split($2,out,":"); for (x in out) print out[x];}'
arg1
arg2
arg3
# substr - 取字符串范围内容;
# 第一个参数是要取的内容, 第二个是开始位置(从1开始),第三个是要取的长度
echo "This is test"|awk '{print substr($3,2,2);}'
es
# sub - 替换原来的字符串,但是只替换第一个符合项; gsub - 替换全部选择项
awk 'BEGIN{str="ThIs is test"; sub("[Ii]s","e", str); print str;}'
The is test
awk 'BEGIN{str="ThIs is test"; gsub("[Ii]s","e", str); print str;}'
The e test
# match - 返回某子字符串是否匹配了某字符串;
# RSTART - awk 自带变量返回匹配的开始位置
# RLENGTH - awk 自带变量返回匹配串的长度
awk 'BEGIN{str="This is test"; if (match(str, "test")) {print substr(str,RSTART,RLENGTH)}}'  
# tolower/toupper - 把字符串都变成小写/大写
awk 'BEGIN{str="This is test"; print tolower(str); print toupper(str);}'
this is test
THIS IS TEST
# ARGC - 参数的数量; ARGV参数的数组
cat arguments.awk
BEGIN {
    print "ARGC=",ARGC
    for (i = 0; i < ARGC; i++)
  print ARGV[i]
}




# ENVIRON - 系统环境变量
cat environ.awk
BEGIN {
 OFS="="
 for(x in ENVIRON)
     print x,ENVIRON[x];
}
# IGNORECASE - 设置为1 忽略大小写
gawk 'BEGIN{IGNORECASE=1} /github/{print}' source.txt
105,Chris Wanstrath,Github




cat bits.awk
BEGIN {
 number1=15
 number2=25
 print "AND: " and(number1,number2);
 print "OR: " or(number1,number2)
 print "XOR: " xor(number1,number2)
 print "LSHIFT: " lshift(number1,2)
 print "RSHIFT: " rshift(number1,2)
}

gawk -f bits.awk
AND: 9
OR: 31
XOR: 22
LSHIFT: 60
RSHIFT: 3					



#自定义函数
# 函数的位置不重要
cat function-debug.awk 

function mydebug (message) {
    print ("Debug Time:" strftime("%a %b %d %H:%M:%S %Z %Y", systime()))
    print (message)
}
{
    mydebug($NF)
}


gawk -f function-debug.awk source.txt

Debug Time:Sat Feb 23 20:53:15 CST 2019
Bicking,Mozilla
Debug Time:Sat Feb 23 20:53:15 CST 2019
Wanstrath,Github
Debug Time:Sat Feb 23 20:53:15 CST 2019
1
Debug Time:Sat Feb 23 20:53:15 CST 2019


#系统调用
# 使用system函数可以调用shell命令
awk 'BEGIN { system("date") }'
Sat Feb 23 20:54:57 CST 2019
# systime 和 strftime上面见过了.处理时间和格式化时间
gawk 'BEGIN { print strftime("%c",systime()) }'
Sat Feb 23 20:55:04 2019




# awk首先读入一行，接着处理getline函数再获得一行....下面显示的就是奇数行
awk -F"," '{print $0;getline;}' source.txt 
101,Ian Bicking,Mozilla
103,Paul Irish,Google
105,Chris Wanstrath,Github
107,Ask Solem Hoel,VMware
# 我们使用getline 并把这行变量赋值给tmp
awk -F, '{getline tmp; print "$0->", $0; print "tmp->", tmp;}' source.txt
$0-> 101,Ian Bicking,Mozilla
tmp-> 102,Hakim El Hattab,Whim
$0-> 103,Paul Irish,Google
tmp-> 104,Addy Osmani,Google
$0-> 105,Chris Wanstrath,Github
tmp-> 106,Mattt Thompson,Heroku
$0-> 107,Ask Solem Hoel,VMware
tmp-> 106,Mattt Thompson,Heroku
# 执行外部程序, close可关闭管道,比如这里必须是`|getline`之前的命令
awk 'BEGIN{"date"| getline;close("date");print "Timestamp:" $0}'
Timestamp:Wed Dec 11 22:41:52 CST 2013
# or
awk 'BEGIN{"date"| getline timestamp;close("date");print "Timestamp:" timestamp}'
Timestamp:Wed Dec 11 22:44:08 CST 2013
