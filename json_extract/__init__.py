# -*- coding: utf-8 -*-
'''
 @file: __init__.py.py
 @Author: Christo
 @time: 2020/11/26 下午8:02
'''
import json


class GetValue2(object):

    def __init__(self,dicts):
        if not isinstance(dicts, dict):
            self.dicts = json.loads(dicts, strict=False)
        else:
            self.dicts = dicts

    def get_values(self, key, default=None,deep=False,filters=False,shell=False,ret_type="int"):
        """
        :param key: Key value to be resolved 需要解析的key值
        :param default: If the result is empty, the default value is none  如果结果为空 备用值 默认None
        :param deep: Do you want to deeply resolve all keys? Default false 是否深度解析所有key 默认False
        :param filters: Whether to de duplicate the result, the default is false 是否去重结果 默认False
        :param shell: If the result is whether to remove the outer list shell, the default is false 如果结果为一个 是否去掉外面list壳子 默认False（去壳）
        :param ret_type: Return result type 返回结果类型
        :return:
        """
        self.filters = filters
        self.str_or_int = ret_type
        self.results = []
        self.deep_search(self.dicts, key) if deep else self.__search(self.dicts, key)
        res = self.flat(self.results)
        if not shell:
            res = res[0] if len(res) == 1 else res
        return default if not res else res

    def __search(self,dicts,key):
        if type(dicts) == list:
            [self.__search(d, key) for d in dicts]
        elif type(dicts) == dict:
            keys_list = dicts.keys()
            if key in keys_list:
                self.results.append(dicts[key])
            else:
                [self.__search(dicts[k], key ) for k in keys_list]

    def deep_search(self,dicts,key):
        if type(dicts) == list:
            [self.deep_search(d, key) for d in dicts]
        elif type(dicts) == dict:
            for k in dicts.keys():
                if k == key:
                    self.results.append(dicts[key])
                else:
                    self.deep_search(dicts[k], key)

    def flat(self,nums):
        res = []
        for i in nums:
            if isinstance(i, list):
                res.extend(self.flat(i))
            else:
                if type(i) == int and self.str_or_int == "str":
                    i = str(i)
                if self.filters:
                    if i not in res:
                        res.append(i)
                else:
                    res.append(i)
        return res
