
# * SOLVED :) * #

import re
def domain_name(url: str):
    url = url.lower()
    
    if url.startswith("http://"):
        res = "".join(re.findall(r"//([\w&-]*).", url))
        if res == "www":
            return "".join(re.findall(r"//www.([\w&-]*).", url))
        return res
    if url.startswith("https://"):
        res = "".join(re.findall(r"//([\w&-]*).", url))
        if res == "www":
            return "".join(re.findall(r"//www.([\w&-]*).", url))
        return res
    if url.startswith("www."):
        return "".join(re.findall(r"www.([\w&-]*).", url))
    else:
        return "".join(re.findall(r"([\w&-]*)\.", url))
    
    

    
for case in ("https://google.com", "https://123.net", "http://google.co.jp", "http://www.codewars.com/kata/", "www.xakep.ru", "icann.org", "https://hyphen-site.org"):
    print(domain_name(case))