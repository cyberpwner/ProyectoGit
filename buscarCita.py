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

driver.implicitly_wait(2);

# accept cookies to remove that whole part from the page
acceptCookies = driver.find_element(By.ID, "cookie_action_close_header");
acceptCookies.click();

# now we need to select which office and the purpose of the appointment
select_element = driver.find_element(By.ID, "sede");
selectOffice = Select(select_element);

# select which office
# select.select_by_visible_text("CNP Alicante TIE, Campo de Mirra, 6");
selectOffice.select_by_value("3");

select_element = driver.find_element(By.ID, "tramiteGrupo[0]");
selectPurpose = Select(select_element);

driver.implicitly_wait(2);

# selectPurpose.select_by_visible_text("POLICIA-TOMA DE HUELLA (EXPEDICIÓN DE TARJETA), RENOVACIÓN DE TARJETA DE LARGA DURACIÓN Y DUPLICADO");
selectPurpose.select_by_value("4010");

nextBtn = driver.find_element(By.ID, "btnAceptar");
nextBtn.click();

# wait and click entrar
driver.implicitly_wait(2);

nextBtn = driver.find_element(By.ID, "btnEntrar");
nextBtn.click();

# my info
myNie = "Y1122330P";
myName = "ANOUAR";
myCountry = "MARRUECOS";

driver.implicitly_wait(2);

# now I have to fill up a form with my info
nie = driver.find_element(By.ID, "txtIdCitado");
nie.send_keys(myNie);

nombre = driver.find_element(By.ID, "txtDesCitado");
nombre.send_keys(myName);

select_element = driver.find_element(By.ID, "txtPaisNac");
selectPais = Select(select_element);

# selectPais.select_by_visible_text(myCountry);
selectPais.select_by_value("348");

# now we click enviar
nextBtn = driver.find_element(By.ID, "btnEnviar");
nextBtn.click();
