"""
This space ready for pylint
"""
import string

MAIL_TEMP = """\

お世話になっております、$name です。

$contents

以上、よろしくお願いいたします。
"""

t = string.Template(MAIL_TEMP)
contents = t.substitute(name='ひろちゃん', contents='お元気ですか')
print(contents)
