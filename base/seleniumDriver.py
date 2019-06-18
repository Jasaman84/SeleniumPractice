from selenium import webdriver
from utilities import custLog
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumDriver():


    def __init__(self,driver):
        self.driver = driver




    log = custLog.custLogger(logging.INFO)

    def getByType(self,locatorType='id'):
        if locatorType.lower() == 'id':
            return By.ID
        elif locatorType.lower() == 'xpath':
            return By.XPATH
        elif locatorType.lower() == 'class':
            return By.CLASS_NAME
        elif locatorType.lower() == 'css':
            return By.CSS_SELECTOR
        elif locatorType.lower() == 'link':
            return By.LINK_TEXT
        elif locatorType.lower() == 'partLink':
            return By.PARTIAL_LINK_TEXT
        elif locatorType.lower() == 'tag':
            return By.TAG_NAME
        else:
            self.log.error(" Locator Type = '%s' is not Supported" %(locatorType))
            return None

    def getElement(self,locator,locatorType='id'):
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)

            self.log.info("Found the element=%s  using  'Locator = %s' and 'Loctor Type = %s'" %(locator,locatorType))
            return element
        except:
            self.log.error("Can not Find the element  using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
            return False

    def isElementPresent(self,locator,locatorType='id'):
        if self.getElement(locator,locatorType) is False:
            self.log.error("Element is not found using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
            return False
        else:
            self.log.info("Element is found using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
            return True

    def clickElement(self,locator,locatorType='id'):
        isElementFound = self.getElement(locator,locatorType)
        if  isElementFound is False:
            self.log.error("Element to Click is not found using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
        else:
            try:
                element = isElementFound
                element.click()
                self.log.info("Clicked the element  using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
                return True
            except:

                self.log.error("Can not click the element  using  'Locator = %s' and 'Loctor Type = %s'"
                              % (locator, locatorType))
                return False

    def typeDataInElement(self,data,locator,locatorType='id'):
        if locatorType.lower() == 'link' or locatorType.lower() == 'partLink':
            self.log.error("Can not enter data in a Link")
        else:

            try:
                element = self.getElement(locator,locatorType)
                element.send_keys(data)
                self.log.info("Entered the data '%s' in element found using  'Locator = %s' and 'Loctor Type = %s'"
                              % (data,locator, locatorType))
                return True
            except:
                self.log.error("Can not Enter data '%s' in element found using  'Locator = %s' and 'Loctor Type = %s'"
                              % (data,locator, locatorType))
                return False

    def selectElement(self,selector,locator,selType='text',locatorType='id'):
        isElementFound=self.getElement(locator,locatorType)

        if  isElementFound is False:
            self.log.error("Element to Select is not found using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
        else:
            try:
                element = isElementFound
                sel = Select(element)
                if selType.lower() == 'index':
                    sel.select_by_index(selector)
                    self.log.info("Selected the option with Selector '%s' and Selector Type '%s' "
                                  % (selector, selType))
                    return True

                elif selType.lower() == 'value':
                    sel.select_by_value(selector)
                    self.log.info("Selected the option with Selector '%s' and Selector Type '%s' "
                                  % (selector, selType))
                    return True

                elif selType.lower() == 'text':
                    sel.select_by_visible_text(selector)
                    self.log.info("Selected the option with Selector '%s' and Selector Type '%s' "
                                  % (selector, selType))
                    return True

                else:
                    self.log.error("Selector Type = '%s' is not supported" %(selType))
                    return False
            except:
                self.log.error("Can not Select the Option with Selector '%s' in the Element found using  'Locator = %s' and 'Loctor Type = %s'"
                              % (selector, locator, locatorType))
                return False

    def getMultipleElements(self, locator, locatorType='id'):
        try:
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            if len(elements) > 0:
                self.log.info("Found the elements using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
                return elements
            else:
                self.log.error(
                    "Can not find elements using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
                return False
        except:
            self.log.error(
                "Can not Find the element  using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
            return False

    def clickMultipleElements(self,locator,locatorType='id'):
        isElementPresent = self.getMultipleElements(locator, locatorType)
        if isElementPresent is False:
           self.log.error("Can not Find the elements to click using  'Locator = %s' and 'Loctor Type = %s'"
                          % (locator, locatorType))
           return False
        else:
            try:
                elements = isElementPresent
                for element in elements:
                    element.click()
                    time.sleep(1)
                self.log.info("Clicked the elements  using  'Locator = %s' and 'Loctor Type = %s'"
                              % (locator, locatorType))
                return True
            except:
                self.log.info(
                    "Can not click the elements found using  'Locator = %s' and 'Loctor Type = %s'"
                    % (locator, locatorType))
                return False



    '''def selectElement(self,text,locator,locatorType='id'):
        isElementFound=self.getElement(locator,locatorType)

        if  isElementFound is False:
            self.log.error("Element to Select is not found using  'Locator = %s' and 'Loctor Type = %s'" % (locator, locatorType))
        else:
            try:
                element = isElementFound
                sel = Select(element)
                sel.select_by_visible_text(text)
                self.log.info("Selected the option with text '%s' in the Element found using  'Locator = %s' and 'Loctor Type = %s'"
                          % (text, locator, locatorType))
                return True
            except:
                self.log.error("Can not Select the Option with text '%s' in the Element found using  'Locator = %s' and 'Loctor Type = %s'"
                              % (text, locator, locatorType))
                return False
                '''
    def selectMultipleElements(self,locator,optionslocator,locatorType='id',optionLocType='css'):
        '''

        :param locator: To locate the Element from which options are to be Selected
        :param optionslocator: To find the options available, This helps us to find total number of options by using
        len(). its then used in FOR loop to iterate through every option
        :param optionLocType='xpath' : Type of optionsLocator

        :param locatorType:
        :return:
        '''
        #find the parent Element from which options are to be selected
        element = self.getElement(locator, locatorType)

        if element is not None:
            try:
                options = self.getMultipleElements(optionslocator,optionLocType)
                sel =Select(element)
                for i in range(0,len(options)):
                    sel.select_by_index(i)
                    time.sleep(2)
                    self.log.info("Selected the optionsat 'index=%s' in the element Found using 'Locator= %s' and 'LocatorType = %s'"
                                  %(i,locator,locatorType))

            except:
                self.log.error(
                    "Can not Select the Options in the Element found using  'Locator = %s' and 'Loctor Type = %s'"
                    % ( locator, locatorType))
                return False

        else:
            self.log.error("Can not Find the element to select using  'Locator = %s' and 'Loctor Type = %s'"
                       % (locator, locatorType))
            return False


def expWait(self, locator, byType, timeout=10, poll_frequency=1):
    try:
        wait = WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions=[NoSuchElementException,
                                                                                       ElementNotVisibleException,
                                                                                       ElementNotSelectableException,
                                                                                       ElementNotInteractableException])
        element = wait.until(EC.element_to_be_clickable((byType, locator)))
        if element is not None:
            self.log.info(f"After wait: Element found by locator ={locator} and byType ={byType}")
            return element
        else:
            self.log.error(f"After wait:Can not find Element by locator ={locator} and byType ={byType}")
            return False

    except:
        self.log.error(f"Failure in wait:Can not find Element by locator ={locator} and byType ={byType}")
        print_stack()
        return False






