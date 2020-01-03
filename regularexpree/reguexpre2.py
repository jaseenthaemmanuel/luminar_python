#quantifiers in regular expression

import re
#x='a+'

#x='a*'

#x='a?'

#x='a{3}'

#x='a{2,3}'

#x='^a'

x='a$'

matcher=re.finditer(x,'abaabaaabacaaab')
for match in matcher:
    print("position",match.start())
    print("group=",match.group())