"""
TODO: 
- modifier la difference en index pour ne tweeter que lorsque le chiffre de dizaines de milliers change
- utiliser l'API twitter
"""


from selenium import webdriver

DIFFERENCE = 50

#get the tree count
driver = webdriver.Chrome('./chromedriver')
driver.get('https://ecosia.org')
content = driver.find_element_by_class_name('js-total-count').text
distant_count = ""
for l in content:
	if not (l == " " or l == "\n"):
		distant_count += l
driver.close()

local_count_file = open("count.txt", "r")
local_count = int(local_count_file.read())
local_count_file.close()
del local_count_file

distant_count = int(distant_count)
if distant_count >= local_count + DIFFERENCE :
	local_count_file = open("count.txt", "w")
	local_count_file.write(str(distant_count))
	local_count_file.close()
	del local_count_file

print("distant_count : "+ str(distant_count))
print("local_count : "+ str(local_count))