# TIL_python

## Naming Convention
![](https://github.com/tkxkd0159/TIL_python/blob/main/img/name.JPG) <br>
class는 ACCRONYM도 가능
```python
# Protection attribute, E.g. from M import * does not import objects whose name starts with an underscore.
_SingleLeadingUnder

# keyword와의 충돌을 피하기 위해 맨 뒤에 붙임. ex) class_ ='ClassName'
SingleTrailingUnder_

# Private attribute, when naming a class attribute, invokes name mangling. (inside class FooBar, __boo becomes _FooBar__boo)
__DoubleLeadingUnder

# Special attributes/method  , ref. Python reference ch.3, 무조건 reference에 있는 것만 사용.
__DoubleLeadingAndTrailingUnder__
```

## Use my custom pkg in any location
`python -m site` 쳐서 site-packages 폴더 중 하나에 pth 파일 추가 <br>
그러면 sys.path에 해당 경로 추가 안해도 내 패키지 폴더 불러올 수 있음

```bash
# mypkgdir.pth
c:\Users\admin\.vscode\extensions\mypkg
mypkg2
mypkg3
...
```
