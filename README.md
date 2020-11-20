# TIL_python

## Naming Convention
![](img/name.jpg)
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