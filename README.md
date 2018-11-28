# pydng
The [Docker name generator](https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go) ported to Python. Just because.

Use it from your shell:
```shell
pip install pydng

pydng
> crazy_faraday
```

Or, use it as a lib:
```shell
python
>>> import pydng
>>> pydng.generate_name()
'vibrant_jackson'
>>>
```
