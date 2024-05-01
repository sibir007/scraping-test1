from selenium.webdriver import Firefox, FirefoxOptions
from . import setings


options = FirefoxOptions()
for k_optin, v_options in setings.OPTIONS.items():
    options.set_preference(k_optin, v_options)

driver = Firefox(options=options)




