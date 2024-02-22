from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.select import Select;

# path to the geckodriver in your machine
driverPath = r"../geckodriver.exe";

# telling the driver to use firefox
driver = webdriver.Firefox();

# go the webpage: cita previa extranjeria
url = "https://icp.administracionelectronica.gob.es/icpplus/index.html";

driver.get(url);

# wait a couple of seconds so that the page is fully loaded
driver.implicitly_wait(6);

# create a select object
select_element = driver.find_element(By.ID, "form");
select = Select(select_element);

# select the option: Alicante
select.select_by_visible_text("Alicante");

# click the button aceptar to continue to the next page
nextBtn = driver.find_element(By.ID, "btnAceptar");
nextBtn.click(); # esta linea hace click en el boton de siguiente/aceptar
