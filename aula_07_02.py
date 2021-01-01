from selenium.webdriver import Firefox
from selenium.webdriver.support.events import(
    AbstractEventListener,
    EventFiringWebDriver,
)

class Escuta(AbstractEventListener):
    def before_click(self,elemento,webdriver):
        if elemento.tag_name =='input'
            print(webdriver.find_element_by_tag_name('p').text)
        print(f'antes do click no {elemento.tag_name}')

    def after_click(self,elemento,webdriver):
        if elemento.tag_name =='input'
            print(webdriver.find_element_by_tag_name('p').text)
        print(f'depois do click no {elemento.tag_name}')

browser = Firefox()

rapi_browser = EventFiringWebDriver(browser,Escuta())

browser.get('https://selenium.dunossauro.live/aula_07_d')

input_de_texto = rapi_browser.find_element_by_tag_name('input')
span=rapi_browser.find_element_by_tag_name('span')
p=rapi_browser.find_element_by_tag_name('p')


input_de_texto.click()
print('Tó clicando')
