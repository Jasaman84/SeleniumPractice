from base.seleniumDriver import SeleniumDriver


class PracticePage(SeleniumDriver):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    radioBtnsLocator = "//div[@id='radio-btn-example']//input[@name='cars' and @type='radio']"
    radioBtnsLocType = 'xpath'
    dropDownLocator ="select#carselect>option"
    dropDownLocType ='css'


    def clickRadioBtns(self):
        self.clickMultipleElements(self.radioBtnsLocator,self.radioBtnsLocType)

    def selectDropDown(self,selector,selType):
        self.selectMultipleElements(self.dropDownLocator,)




