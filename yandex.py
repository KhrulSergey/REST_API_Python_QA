#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import unittest
import requests
import datetime
import locale
import pytils
from enum import Enum

locale.setlocale(locale.LC_ALL, 'russian_russia')


class TransportTypeEnum(Enum):
   All = 1
   Plane = 2
   Train = 3
   Electric_train = 4
   Bus = 5


class DayOfWeek(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


# Search for next day
def get_next_weekday(startdate, weekday):
    """
    @startdate: given date, in datetime.date format
    @weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
    """
    t = datetime.timedelta((7 + weekday - startdate.weekday()) % 7)
    return startdate + t


class CheckResultTitle(Enum):
    IsNone = "Введены не корректные данные. В результате обработки возникли ошибки."
    IsFalse = "Данные о рейсах не найдены. Измените пожалуйста запрос."


def is_title_ya_rasp_correct(title, from_city, to_city, departure_date=datetime.date.today(), transport_type=TransportTypeEnum.All):
    # check if parameters is eligible
    if title and from_city and to_city:
        # convert date to right string in Russian
        date_str = pytils.dt.ru_strftime(u"%d %B", date=departure_date, inflected=True)
        # check if title with right date
        if date_str in title:
            # check if title with right Cities
            if from_city in title and to_city in title:
                # check if title with zero results
                if "не найдено" in title:
                    return False
                else:
                    if transport_type == TransportTypeEnum.All:
                        return True
                    if transport_type == TransportTypeEnum.Train and "поезд" in title:
                        return True
                    if transport_type == TransportTypeEnum.Electric_train and "электричек" in title:
                        return True
                    if transport_type == TransportTypeEnum.Bus and "автобус" in title:
                        return True
                    if transport_type == TransportTypeEnum.Plane and "самолёт" in title:
                        return True
    # if we didn't find right match between parameters return None as indicator of Error
    return None

# Все
# consist of: $From && $To && %d %B

# Электричка
# consist of: $From && $To && электричек && %d %B
# consist of: %d %B && не найдено
#
# # Поезд
# consist of: $From && $To && поезд  && %d %B
# consist of: %d %B && не найдено

# Автобус
# consist of: $From && $To && автобус && %d %B
# consist of: %d %B && не найдено

# Самолет
# consist of: %d %B && не найдено
# consist of: $From && $To && самолёт && %d %B


class TripData:
    def __init__(self):
        self.departure_time = datetime.date.today()
        self.arrival_time = datetime.date.today()
        self.fmt = '%H:%M:%S'
        self.trip_time = datetime.time(1)
        self.price_in_rub = 0
        self.price_in_usd = 0
        self.departure_point = ""
        self.arrival_point = ""


class Rasp(unittest.TestCase):
    # Date of schedule search
    DepartureDate = datetime.date(2018, 4, 14)

    # Format of viewing date
    DateFormat = '%d.%m.%Y'

    # Start date of departure (schedule search)
    Departure_Day_of_Week = DayOfWeek.Saturday

    # Departure city
    Departure_city = "Екатеринбург"

    # Destination city
    Destination_city = "Каменск-Уральский"

    # Minimal ticket cost
    Cost_of_ticket = 200

    # Type of transport to search schedule
    Transport_type = TransportTypeEnum.Electric_train

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(100)

        self.verificationErrors = []
        self.accept_next_alert = True

    def test_rasp(self):
        departure_date = get_next_weekday(datetime.date.today(), self.Departure_Day_of_Week.value)
        departure_date_str = pytils.dt.ru_strftime(u"%d %B", date=departure_date, inflected=True)
        driver = self.driver

        driver.get("https://www.yandex.ru/")
        driver.find_element_by_link_text("еще").click()
        # data - id = "rasp"
        rasp_but = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Расписания")))
        rasp_but.click()
        # driver.find_element_by_link_text("Расписания").click()

        transport_type_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[" + str(self.Transport_type.value) + "]")))
        transport_type_button.click()
        from_name = driver.find_element_by_name("fromName")
        from_name.clear()
        from_name.send_keys(self.Departure_city)
        to_name = driver.find_element_by_name("toName")
        to_name.clear()
        to_name.send_keys(self.Destination_city)

        s1 = "document.getElementsByName('when')[0].value='" + departure_date_str + "'"
        driver.execute_script(s1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        submit_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//button[@type='submit']")))
        submit_btn.click()
        driver.set_page_load_timeout(95)
        driver.set_script_timeout(95)

        WebDriverWait(driver, 20).until(EC.title_contains(departure_date_str))
        check_title_result = is_title_ya_rasp_correct(driver.title, self.Departure_city, self.Destination_city,
                                                        departure_date, self.Transport_type)
        print(check_title_result)

        if check_title_result:
            mass = driver.find_elements_by_css_selector("//article[@class ='SearchSegment SearchSegment_isNotInterval "
                                                        "SearchSegment_isNotGone SearchSegment_isVisible']")
            print(mass)
        elif check_title_result is None:
            print(CheckResultTitle.IsNone.value)
        else:
            print(CheckResultTitle.IsFalse.value)


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


# def wait_for_ajax(self, xpath, timeout=5):
#     wait = WebDriverWait(self.driver, timeout=int(timeout))
#     message = "Element '%s' was not visible in %s second(s)." % (xpath, str(timeout))
#     wait.until(lambda driver: driver.find_element_by_xpath(xpath).is_displayed()
#                               and driver.execute_script("return $.active") == 0, message=message)
#
#
# def explict_wait():
# timeout = time.time() + timeout.
# while time.time() < timeout:
# try:
# find_element
# do action with element
# except StaleElementReferenceException:
# pass
