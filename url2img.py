from html2image import Html2Image
hti = Html2Image()

html = '<h1> A title </h1> Some text.'
css = 'body {background: red;}'

# screenshot an HTML string (css is optional)
hti.screenshot(html_str=html, css_str=css, save_as='page.png')

# screenshot an URL
hti.screenshot(url='https://en.wikipedia.org/wiki/The_World%27s_Billionaires', save_as='python_org.png')