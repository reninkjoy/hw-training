from requests_html import HTML,HTMLSession
import json
session= HTMLSession()
r=session.get("https://www.bayut.com/to-rent/property/dubai/")
# print(help(r))
def links():
	lik=[]
	lin=r.html.find('article')
	for link in lin:
		lik.append(link.links)
		# print(lik)
	return lik

def main():
	# lin=r.html.find('.b7880daf')
	# for link in lin:
	# 	nextl=link.links if link.attrs['title']=="Next" else print()
	# print(nextl)	
	# r.get_redirect_target(nextl)
	ulrs=links()
	print(ulrs)
if __name__=="__main__":
    main() 
