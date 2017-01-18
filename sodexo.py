import requests
from lxml import html

class SodexoApi:
  def __init__(self, email, password):
    self.session = requests.Session()
    self.login(email, password)

  def login(self, email, password):
    payload = {
      'email': email,
      'password': password
    }
    self.session.post('https://cardsodexo.ro/login/process', data=payload)

  def get_balance(self):
    page = self.session.get('https://cardsodexo.ro/contul-meu')
    tree = html.fromstring(page.text)
    return tree.xpath('.//div[@class="contSidebar"]//h4//span/text()')[0]
