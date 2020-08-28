from selenium.webdriver import Firefoxcd
def find_element_by_text(browser,tag, text):
    """
    Encontrar o elemento com o texto

    argumentos/:
        -browser = instancia do browser
        -text= o elemento o conteudo q deve esta na teg
        -tag = onde o texto sera procutado

    """
    browser.find_element_by_tag_name(tag)#imprime uma lista_n_ordenada

    for elemento in elementos:
        if elemento.txt == text:
            return elemento

browser = Firefox()

elemento_ddg = find_by_text(browser, 'li', 'DuckDucGo')
