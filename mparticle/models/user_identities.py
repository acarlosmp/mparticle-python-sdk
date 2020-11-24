# coding: utf-8

"""
    mParticle

    mParticle Event API

    OpenAPI spec version: 1.0.1
    Contact: support@mparticle.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class UserIdentities(object):

    def __init__(self, other=None, customerid=None, facebook=None, twitter=None, google=None, microsoft=None, yahoo=None, email=None, alias=None, facebook_custom_audience_id=None, other_id_2=None, other_id_3=None, other_id_4=None, other_id_5=None, other_id_6=None, other_id_7=None, other_id_8=None, other_id_9=None, other_id_10=None, mobile_number=None, phone_number_2=None, phone_number_3=None):
        """
        UserIdentities - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'other': 'str',
            'customerid': 'str',
            'facebook': 'str',
            'twitter': 'str',
            'google': 'str',
            'microsoft': 'str',
            'yahoo': 'str',
            'email': 'str',
            'alias': 'str',
            'facebook_custom_audience_id': 'str',
            'other_id_2': 'str',
            'other_id_3': 'str',
            'other_id_4': 'str',
            'other_id_5': 'str',
            'other_id_6': 'str',
            'other_id_7': 'str',
            'other_id_8': 'str',
            'other_id_9': 'str',
            'other_id_10': 'str',
            'mobile_number': 'str',
            'phone_number_2': 'str',
            'phone_number_3': 'str'
        }

        self.attribute_map = {
            'other': 'other',
            'customerid': 'customerid',
            'facebook': 'facebook',
            'twitter': 'twitter',
            'google': 'google',
            'microsoft': 'microsoft',
            'yahoo': 'yahoo',
            'email': 'email',
            'alias': 'alias',
            'facebook_custom_audience_id': 'facebook_custom_audience_id',
            'other_id_2': 'other_id_2',
            'other_id_3': 'other_id_3',
            'other_id_4': 'other_id_4',           
            'other_id_5': 'other_id_5',
            'other_id_6': 'other_id_6',
            'other_id_7': 'other_id_7',        
            'other_id_8': 'other_id_8',
            'other_id_9': 'other_id_9',
            'other_id_10': 'other_id_10',           
            'mobile_number': 'mobile_number',
            'phone_number_2': 'phone_number_2',
            'phone_number_3': 'phone_number_3'
        }

        self._other = other
        self._customerid = customerid
        self._facebook = facebook
        self._twitter = twitter
        self._google = google
        self._microsoft = microsoft
        self._yahoo = yahoo
        self._email = email
        self._alias = alias
        self._facebook_custom_audience_id = facebook_custom_audience_id
        self._other_id_2 = other_id_2
        self._other_id_3 = other_id_3
        self._other_id_4 = other_id_4
        self._other_id_5 = other_id_5
        self._other_id_6 = other_id_6
        self._other_id_7 = other_id_7
        self._other_id_8 = other_id_8
        self._other_id_9 = other_id_9
        self._other_id_10 = other_id_10
        self._mobile_number = mobile_number
        self._phone_number_2 = phone_number_2
        self._phone_number_3 = phone_number_3

    @property
    def other(self):
        """
        Gets the other of this UserIdentities.


        :return: The other of this UserIdentities.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """
        Sets the other of this UserIdentities.


        :param other: The other of this UserIdentities.
        :type: str
        """

        self._other = other

    @property
    def customerid(self):
        """
        Gets the customerid of this UserIdentities.


        :return: The customerid of this UserIdentities.
        :rtype: str
        """
        return self._customerid

    @customerid.setter
    def customerid(self, customerid):
        """
        Sets the customerid of this UserIdentities.


        :param customerid: The customerid of this UserIdentities.
        :type: str
        """

        self._customerid = customerid

    @property
    def facebook(self):
        """
        Gets the facebook of this UserIdentities.


        :return: The facebook of this UserIdentities.
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """
        Sets the facebook of this UserIdentities.


        :param facebook: The facebook of this UserIdentities.
        :type: str
        """

        self._facebook = facebook

    @property
    def twitter(self):
        """
        Gets the twitter of this UserIdentities.


        :return: The twitter of this UserIdentities.
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """
        Sets the twitter of this UserIdentities.


        :param twitter: The twitter of this UserIdentities.
        :type: str
        """

        self._twitter = twitter

    @property
    def google(self):
        """
        Gets the google of this UserIdentities.


        :return: The google of this UserIdentities.
        :rtype: str
        """
        return self._google

    @google.setter
    def google(self, google):
        """
        Sets the google of this UserIdentities.


        :param google: The google of this UserIdentities.
        :type: str
        """

        self._google = google

    @property
    def microsoft(self):
        """
        Gets the microsoft of this UserIdentities.


        :return: The microsoft of this UserIdentities.
        :rtype: str
        """
        return self._microsoft

    @microsoft.setter
    def microsoft(self, microsoft):
        """
        Sets the microsoft of this UserIdentities.


        :param microsoft: The microsoft of this UserIdentities.
        :type: str
        """

        self._microsoft = microsoft

    @property
    def yahoo(self):
        """
        Gets the yahoo of this UserIdentities.


        :return: The yahoo of this UserIdentities.
        :rtype: str
        """
        return self._yahoo

    @yahoo.setter
    def yahoo(self, yahoo):
        """
        Sets the yahoo of this UserIdentities.


        :param yahoo: The yahoo of this UserIdentities.
        :type: str
        """

        self._yahoo = yahoo

    @property
    def email(self):
        """
        Gets the email of this UserIdentities.


        :return: The email of this UserIdentities.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserIdentities.


        :param email: The email of this UserIdentities.
        :type: str
        """

        self._email = email

    @property
    def alias(self):
        """
        Gets the alias of this UserIdentities.


        :return: The alias of this UserIdentities.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this UserIdentities.


        :param alias: The alias of this UserIdentities.
        :type: str
        """

        self._alias = alias

    @property
    def facebook_custom_audience_id(self):
        """
        Gets the facebook_custom_audience_id of this UserIdentities.


        :return: The facebook_custom_audience_id of this UserIdentities.
        :rtype: str
        """
        return self._facebook_custom_audience_id

    @facebook_custom_audience_id.setter
    def facebook_custom_audience_id(self, facebook_custom_audience_id):
        """
        Sets the facebook_custom_audience_id of this UserIdentities.


        :param facebook_custom_audience_id: The facebook_custom_audience_id of this UserIdentities.
        :type: str
        """

        self._facebook_custom_audience_id = facebook_custom_audience_id

    @property
    def other_id_2(self):
        return self._other_id_2

    @other_id_2.setter
    def other_id_2(self, other_id_2):
        self._other_id_2 = other_id_2


    @property
    def other_id_3(self):
        return self._other_id_3

    @other_id_3.setter
    def other_id_3(self, other_id_3):
        self._other_id_3 = other_id_3


    @property
    def other_id_4(self):
        return self._other_id_4

    @other_id_4.setter
    def other_id_4(self, other_id_4):
        self._other_id_4 = other_id_4


    @property
    def other_id_5(self):
        return self._other_id_5

    @other_id_5.setter
    def other_id_5(self, other_id_5):
        self._other_id_5 = other_id_5


    @property
    def other_id_6(self):
        return self._other_id_6

    @other_id_6.setter
    def other_id_6(self, other_id_6):
        self._other_id_6 = other_id_6


    @property
    def other_id_7(self):
        return self._other_id_7

    @other_id_7.setter
    def other_id_7(self, other_id_7):
        self._other_id_7 = other_id_7


    @property
    def other_id_8(self):
        return self._other_id_8

    @other_id_8.setter
    def other_id_8(self, other_id_8):
        self._other_id_8 = other_id_8


    @property
    def other_id_9(self):
        return self._other_id_9

    @other_id_9.setter
    def other_id_9(self, other_id_9):
        self._other_id_9 = other_id_9


    @property
    def other_id_10(self):
        return self._other_id_10

    @other_id_10.setter
    def other_id_10(self, other_id_10):
        self._other_id_10 = other_id_10


    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        self._mobile_number = mobile_number


    @property
    def phone_number_2(self):
        return self._phone_number_2

    @phone_number_2.setter
    def phone_number_2(self, phone_number_2):
        self._phone_number_2 = phone_number_2


    @property
    def phone_number_3(self):
        return self._phone_number_3

    @phone_number_3.setter
    def phone_number_3(self, phone_number_3):
        self._phone_number_3 = phone_number_3


    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
