import logging
import yndex
yndx = yndex.yndex("https://www.ya.ru'")
logging.basicConfig(filename='yandex.log', level=logging.DEBUG)

def test1():
    try:
        assert yndx.load_yandex() == True
        assert yndx.go_links() == True
        assert yndx.load_picte() == True
        assert yndx.click_picche() == True
        assert yndx.category() == True
        assert yndx.click_picte1() == True
        assert yndx.lload == True
        assert yndx.load_button == True
        assert yndx.click_button_back == True
        logging.debug(f'test error')
    except:    
        logging.debug(f'test error')