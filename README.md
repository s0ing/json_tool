![PyPI - Python Version](https://img.shields.io/badge/python-3.0%2B-blue)

**安装 json_extract**

> pip install json-extract

```angular2
response_json = {
    "animals": {
        "zoon": [
            {
                "name": "Peki",
                "sex": 'girl'
            },
            {
                "name": "George",
                "sex": 'boy'
            }
        ],
        "people": [
            {
                "name": "Rufus",
                "sex": 'girl'
            },
            {
                "name": "Marty",
                "sex": 'boy',
                "people": [
                            {
                                "name": "Rufus",
                                "sex": 'peoplegirl'
                            },
                            {
                                "name": "Marty",
                                "sex": 'peopleboy'
                            }]
            }]

    }
    }
```

        from json_extract import GetValue2
        getobj = GetValue2(response_json)
        sex = getobj.get_values('sex')
        print(sex)
        ['girl', 'boy', 'girl', 'boy']

### End