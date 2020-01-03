import re
#x='\s'

#x='\d'

#x='\D'

#x='\w'

x='\W'

matcher=re.finditer(x,'a7b @k9az')
for match in matcher:
    print("match available at",match.start())
    print("group=",match.group())