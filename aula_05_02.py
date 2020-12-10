from selenium.webdriver import Firefox
url = 'http://selenium.dunossauro.live/aula_05_a.html'

firefox = Firefox()

firefox.get(url)

topico =firefox.find_element_by_class_name('topicos')
linguagens =firefox.find_element_by_class_name(  'linguagens')

for linguagen in linguaens:
    print(linguagen.find_element_by_tag_name('h2').text,
    linguagen.find_element_by_tag_name('p').text)
