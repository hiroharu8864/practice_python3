import string

mail_temp = """\

お世話になっております、$name です。

$contents

以上、よろしくお願いいたします。
"""

t = string.Template(mail_temp)
contents = t.substitute(name='ひろちゃん', contents='お元気ですか')
print(contents)
