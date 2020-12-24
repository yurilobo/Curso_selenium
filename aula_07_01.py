from selenium.webdriver import Firefox

"""
Chercar se a mudanca ocorre no span(focus,bur)
checar se a mudanca ocorre no p(change)
"""



browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_07_d')

input_de_texto = browser.find_element_by_tag_name('input')
span=browser.find_element_by_tag_name('span')
p=browser.find_element_by_tag_name('p')


input_de_texto.click()
assert 'está com foco'== span.text,'esta com foco não esta em span'
span.click()
assert 'está sem foco'== span.text,'esta sem foco não esta em span'

"""
quando o texto '0' p content deve ser p
quando enviar "batata" no elemento input
entao o texto "esta com foco " deve ser o content de span
clicar no span
o texto 'esta sem foco ' dever ser o content de 'span'
o texto '1 ' serao conteudo de 'p'

"""

assert p.text== '0','p não é zero'
input_de_texto.send_keys('batata')
assert 'está com foco'== span.text,'esta com foco não esta em span'
span.click()
assert 'está sem foco'== span.text,'esta sem foco não esta em span'
assert p.text =='1', 'p não é um'

browser.quit()
