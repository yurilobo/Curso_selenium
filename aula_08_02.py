from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://selenium.dunossauro.live/aula_08_a'
texto ='selenium'

browser = Firefox()
browser.get(url)
#hi-level
elemento = browser.find_element_by_name('texto')
elemento.send_keys('selenium')
#low level
ac = ActionChains(browser)
ac.move_to_element(elemento)
ac.click(elemento)
ac.key_down(u'\ue008')

for letra in texto:
    ac.key_down(letra)
    ac.key_up(letra)

ac.key_up(u'\ue008')

ac.perform()
