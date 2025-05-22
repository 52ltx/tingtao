
from services.link_convert.parser import parse_content

old_content = '''
先锁单，再犹豫!!!
补贴5.5虹包！=12.8亓，
任选男女都有，Artsdon
阿仕顿棉100%纯棉短袖T恤，
/U4tkVkdwJab// HU108
'''

new_content = parse_content(old_content)
print(new_content)