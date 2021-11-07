import os
from selenium import webdriver
from jobs.contant import BASE_URL

class Jobs(webdriver.Chrome):
    def __init__(self, driver_path= r"C:/SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] = self.driver_path
        super(Jobs, self).__init__()
        self.maximize_window()
        self.implicitly_wait(15)

    def land_first_page(self):
        self.get(BASE_URL)

    def search_by_skills(self,skill):
        search_field = self.find_element_by_id('txtKeywords')
        search_field.clear()
        search_field.send_keys(skill)

        submit_btn = self.find_element_by_css_selector(
            'button[onclick="javascript:setAClickOnSearch();"]'
        )        
        submit_btn.click()

    def search_by_skills_location(self, skill, location):
        
        search_field = self.find_element_by_id('txtKeywords')
        search_field.clear()
        search_field.send_keys(skill)
        
        location_field = self.find_element_by_id("txtLocation")
        location_field.clear()
        location_field.send_keys(location)

        submit_btn = self.find_element_by_css_selector(
            'button[onclick="javascript:setAClickOnSearch();"]'
        )        
        submit_btn.click()

    def search_by_skills_location_experience(self, skill, location, exp):
        
        search_field = self.find_element_by_id('txtKeywords')
        search_field.clear()
        search_field.send_keys(skill)
        
        location_field = self.find_element_by_id("txtLocation")
        location_field.clear()
        location_field.send_keys(location)

        exp_field = self.find_element_by_id("cboWorkExp1")
        exp_field.click()

        exp_option = exp_field.find_element_by_css_selector(f'option:nth-child({2+exp})')
        exp_option.click()

        submit_btn = self.find_element_by_css_selector(
            'button[onclick="javascript:setAClickOnSearch();"]'
        )        
        submit_btn.click()    
        
