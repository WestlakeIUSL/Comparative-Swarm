# Comparative使用说明

## 前述

​	本仓库的大框架是fork了MetaGPT的仓库, 因为其文件体量最大, 其他用于对比试验的还有Code as Policies(只有1个python文件), GPT(只有1一个python文件), 由于CaP和GPT的文件量为最低单位, 不再新开一个仓库, 都放在了该仓库中, 一起做对比试验

​	注意, 要使用v0.8-release分支, main分支暂时有bug不要使用

## 文件夹说明

- CaP: 存储了用于对比试验的CaP的代码(暂时还没加入)
- GPT4: 存储了用于做对比试验的GPT的代码
- metagpt: 存储了做对比试验的MetaGPT的主体代码
- config: 用于配置集群任务, LLM的api信息
- swarm_prompt: 存储了集群任务的全部提示词
- workspace: 内部将会有CaP, GPT4, metagpt三个子文件夹, 分别存储各自的对比试验生成的代码
- requirements.txt: 依赖包
- 根目录下其他文件夹和文件: 均为metagpt的自带文件, 不必关注

## 环境说明

python =3.10

```
conda create -n comparative_codellm_py310 python=3.10
```

```
conda activate comparative_codellm_py310
```

```
pip install -r requirements.txt
```

## 如何运行

### metagpt

​	metagpt需要关注这几个文件夹: 

- config/config2.yaml: 在这里设置LLM的网址和API, 注意, 网址要有/v1后缀
- config/experiment_config.yaml: 这里设置集群任务 task_name
- metagpt/multi_run.py: 主函数入口, 可以设置运行几次softward_company.py文件, 也就生成几份代码
- metagpt/software_company.py: 这里在startup()函数的idea中输入集群任务指令 user_requirements
- metagpt/acions/action.py: 在这里set_prefix()函数中 设置system_prompt, 输入集群环境描述/机器人API等要求

使用安装好依赖的python环境直接运行multi_run.py即可在workspace中得到对应的集群控制代码

***





