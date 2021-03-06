- [Naming Convention](#naming-convention)
- [Module & Package](#module--package)
  - [Use my custom pkg in any location](#use-my-custom-pkg-in-any-location)
- [Design Pattern](#design-pattern)
  - [Decorator pattern](#decorator-pattern)
  - [Observer pattern](#observer-pattern)
  - [Singleton pattern](#singleton-pattern)
- [JSON 처리](#json-처리)
```
dir()  # return the names in the current scope
```
# Naming Convention
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
# Module & Package
package 내에서는 서로 상대경로 참조 가능 <br>
특정 파일을 실행할 때 그 파일의 `__name__`은 `__main__`이 되고 이 파일에 대한 절대경로가 생성됨. <br>
이를 기준으로 프로젝트 내의 package들을 절대경로로 import 할 수 있음(+ sys.path의 packages)
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

# Design Pattern
`design_patter.py` 참조 
## Decorator pattern
```python
class C(object):
    @my_decorator
    def method(self):
        # method contents
```
## Observer pattern
object의 one-to-many 의존 관계에서 한 object의 상태가 변경되면, 그 객체에 종속된 모든 객체에 그 내용을 통지하여 자동으로 상태를 갱신하는 방식

## Singleton pattern
해당 object의 instance가 하나만 존재하게 하는 것

# JSON 처리
```python
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
#convert to JSON
y = json.dumps(y)
print(f'{y} {type(y)}')
```
