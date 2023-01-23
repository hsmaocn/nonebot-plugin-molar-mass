# nonebot-plugin-molar-mass

本项目为 `Nonebot2` 插件，用来计算摩尔质量或相对分子质量。

因为我每次遇到计算题都要去翻课本，然后按计算器，不胜其烦，导致了这个库的出现。

可以查看本项目的 `CLI` 分支，直接使用 `cli` 版本。

# 安装

使用 `pip` 安装：

```bash
> pip install nonebot-plugin-molar-mass
```

使用 `nb-cli` 安装：

```bash
> nb plugin install nonebot-plugin-molar-mass
```

# 使用

发送 `/摩尔质量 化学式` 或者 `/相对分子质量 化学式`，以下为几组输入输出的例子：

```
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
```

注意，这里的斜杠指的是 `COMMAND_START`，你可以参考 Nonebot 官方文档配置这个选项。
