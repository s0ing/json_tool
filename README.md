>	我们在提取json串中的某个值得时候难免会碰到一层一层又一层的嵌套 想要提取要一层一层的找key 像剥洋葱一样
>今天安利一款暴力提取库 json_extract 

*极速上手教程*

**安装 json_extract**

> pip install json-extract

```json
{
    "animals": {
        "zoon": [
            {
                "name": "Peki",
                "sex": "girl",
                "age": 18
            },
            {
                "name": "George",
                "sex": "boy",
                "type":"zoon"

            }
        ],
        "people": [
            {
                "name": "Rufus",
                "sex": "girl",
                "weight":"88"
            },
            {
                "name": "Marty",
                "sex": "boy",
                "people": [
                            {
                                "name": "Rufus",
                                "type":"people",
                            },
                            {
                                "name": "Marty",
                                "sex": "？？？",
                                "age": "10"
                            }]
            }]

    }
    }

```

```python
response_json={}
from json_extract import GetValue2
getobj = GetValue2(response_json)

sex = getobj.get_values('sex')
print(sex)
# ['girl', 'boy', 'girl', 'boy']

deep = getobj.get_values("sex",deep=True)
# ['girl', 'boy', 'girl', 'boy', '？？？']

filte = getobj.get_values("sex",filters=True)
# ['girl', 'boy']

notexiste = getobj.get_values("asdfadfs",default='not existe')
# or
getobj.get_values("asdfadfs",'not existe')
# not existe

weight = getobj.get_values("weight")
# 88
weight_shell = getobj.get_values("weight",shell=True)
# ['88']

age = getobj.get_values("age")
# [18, '10']

age_int = getobj.get_values('age',ret_type=int)
# [18, 10]

age_str = getobj.get_values("age",ret_type=str)
# ['18', '10']




```


```text
:param key: Key value to be resolved 需要解析的key值
:param default: If the result is empty, the default value is none  如果结果为空 备用值 默认None
:param deep: Do you want to deeply resolve all keys? Default false 是否深度解析所有key 默认False
:param filters: Whether to de duplicate the result, the default is false 是否去重结果 默认False
:param shell: If the result is whether to remove the outer list shell, the default is false 如果结果为一个 是否去掉外面list壳子 默认False（去壳）
:param ret_type: The return result type can pass in 'int' or 'str' by default  返回结果类型 可传入'int'或'str' 默认原始
```

[✫传送门](https://github.com/TIM952597205/json_tool)
### End