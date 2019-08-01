class HomePage():

    def __init__(self, driver):
        self.driver= driver

        self.user_specific_url= "https://stportal.victorops.com/client/sdet"

        def check_current_url():
            return self.driver.current_url
