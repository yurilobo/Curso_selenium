from selenium.webdriver import Firefox

b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06.html'

b.get(url)


b.find_element_by_css_selector('.form-l1c1 input[name="nome"]').send_keys('Anderson')
