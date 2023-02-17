# Alfred_Workflows-TimeStamp_Convert

- 参考的 [codezm](https://github.com/codezm/Alfred-codezm-workflows-timestamp-convert) 的 php 版本
- strtotime 参考自: [python 实现 php 中的 strtotime
  ](https://www.cnblogs.com/wallywl/p/15028130.html)

新版 MacOS 移除了系统内置的 PHP 环境, codezm 的插件无法正常使用,同时新版本的 MacOS 的内置 python 由 python2 升级到了 python3,遂用 Python 开发.

## 时间戳转换工具

默认快捷键`t`，查看当前时间格式展示。

### 效果

!["Alfred-codezm-workflows-timestamp-convert Demo"](demo.gif)

### 下载

[点击下载]()

### 安装

下载后直接双击导入即可.

### 使用

- 默认展示当天时间信息.
- 你也可以使用 `t tomorrow` `t yesterday`, 更多格式[参见](http://php.net/manual/en/datetime.formats.relative.php).
- 将时间戳转换成日期格式, 反之亦然 `t 1495276608` `t 2017-05-20 18:52:46`.
- 选中某一项转换结果键入 `Enter` 即可复制, `Shift + Enter` 将发音.
