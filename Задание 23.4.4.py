# Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:

"""
<html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
"""

import lxml.html

html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''

tree = lxml.html.document_fromstring(html)

text = tree.xpath('/html/body/tag1/tag2/text()')
print(text)

