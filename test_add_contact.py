# -*- coding: utf-8 -*-
from fill_forms_construction.contact import *
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user="admin", password="secret")
    app.fill_name(Contact(name_frst="Petr",
                          name_mdl="Petrovych",
                          name_lst="Petrov",
                          name_nick="PetrCompNick"))
    app.title_company_address(Contact(comp_title="PetrComp_1111",
                                      comp_name="PetrComp",
                                      comp_addr="Ulica 2"))
    app.phones(Contact(home_ph="111-111-111",
                       mobile_ph="222-222-222",
                       work_ph="333-333-333",
                       fax_ph="444-444-444"))
    app.emails_homepage(Contact(email_1="111111@example.com",
                                email_2="222222@example.com",
                                email_3="333333@example.com",
                                home_page="example.com"))
    app.anniversary_group(Contact(b_day="3",
                                  b_month="March",
                                  b_year="2000",
                                  a_day="4",
                                  a_month="February",
                                  a_year="2010"))
    app.secondary(Contact(secondary_address="Secondary Address unknown",
                          secondary_phone="Secondary phone ?",
                          secondary_notes="Secondary notes"))
    app.logout()


def test_add_empty_contact(app):
    app.login(user="admin", password="secret")
    app.fill_name(Contact(name_frst="",
                          name_mdl="",
                          name_lst="",
                          name_nick=""))
    app.title_company_address(Contact(comp_title="",
                                      comp_name="",
                                      comp_addr=""))
    app.phones(Contact(home_ph="",
                       mobile_ph="",
                       work_ph="",
                       fax_ph=""))
    app.emails_homepage(Contact(email_1="",
                                email_2="",
                                email_3="",
                                home_page=""))
    app.secondary(Contact(secondary_address="",
                          secondary_phone="",
                          secondary_notes=""))
    app.logout()
