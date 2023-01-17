# 概述

这是一个帮助中学生快速计算相对分子质量的工具。

因为我每次遇到计算题都要去翻课本，然后按计算器，不胜其烦，导致了这个库的出现。

# 使用方法

本项目使用 `poetry` 进行包管理，所以先安装它：

```bash
> pip install -U poetry
```

然后安装本项目需要的包，并且使用 `poetry` 的环境来运行 `main.py`：

```bash
> poetry install
> poetry run python main.py
```

你也可以激活 `poetry` 环境，具体方式请查询 `poetry` 的[官方文档](https://python-poetry.org/docs/)。


输入 `exit` 或 `quit` 退出，水合物用加号 `+` 连接：

```bash
$ python main.py
> NaOH
40
> H2SO4
98
> 2HCl
73
> (NH4)2SO4
132
> CuSO4+5H2O
250
> exit
```

# 总结

Just for fun.

估计打开电脑，找到指定目录，然后运行的时间都做完好几道选择题了。