# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" VERSION 2: Sample App Engine application demonstrating how to connect to Google Cloud SQL
using App Engine's native unix socket or using TCP when running locally.

Author: 	Ruairidh Barlow
Author: 	Jay Gandhi
Project:    Valet Database
Course:     CMSC 508
"""

# [START all]
import os
import MySQLdb
import webapp2

# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')


def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD)

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
    else:
        db = MySQLdb.connect(
            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD)

    return db


class MainPage(webapp2.RequestHandler):
    def get(self):
        """Simple request handler that shows all of the MySQL variables."""
        self.response.headers['Content-Type'] = 'text/plain'

        db = connect_to_cloudsql()
        cursor = db.cursor()
        cursor.execute('SHOW DATABASES')
        cursor.execute('USE VALET')

        """OLD CODE"""

        # cursor.execute('INSERT INTO GUEST VALUES(%s, %s, %s)',(956246, 'Patricia', 'Smith'))
        # NORMAL INSERT COMMAND

        # The query INSERT STATEMENT USING THE VIEW "INSERT_GUEST"
        # cursor.execute('INSERT INTO INSERT_GUEST VALUES(%s, %s, %s)',(956241, 'Andy', 'Griffin'))

        # cursor.execute('SELECT * FROM GUEST')

        # The query below will display the GuestID of the guest staying in RoomNumber 101
        # SELECT_QUERY = 'SELECT GuestID FROM STAY WHERE RoomNumber = 101'
        # cursor.execute(SELECT_QUERY)

        # The query below updates the DepartureDate of a Guest Given their GuestID
        # UPDATE_QUERY = "UPDATE STAY SET DepartureDate = CURDATE() WHERE GuestID = 'DBS508'"
        # cursor.execute(UPDATE_QUERY)
        # cursor.execute('SELECT * FROM STAY')

        # The query below removes a guest from the GUEST table given their GuestID
        # DELETE_QUERY = "DELETE FROM GUEST WHERE GuestID = '956243'"
        # cursor.execute(DELETE_QUERY)
        # cursor.execute('SELECT * FROM GUEST')
        # db.commit()

        """QUERIES"""

        # QUERY_1 = 'SELECT V.Manufacturer , V.Model FROM VEHICLE V JOIN TICKET T ON T.TicketNumber = V.TicketNumber WHERE T.TicketNumber = 567894'
        # cursor.execute(QUERY_1)
        # self.response.write('MANUFACTUERE, MODEL\n')

        # QUERY_2 = 'SELECT GuestID FROM STAY WHERE RoomNumber = 101'
        # cursor.execute(QUERY_2)
        # self.response.write('GuestID\n')

        # QUERY_3 = "SELECT S.GuestID, S.RoomNumber, S.ArrivalDate, S.DepartureDate, S.RoomPhoneNumber FROM STAY S JOIN GUEST G ON G.GuestID = S.GuestID WHERE G.FirstName = 'Mary'  and G.LastName = 'Jane'"
        # cursor.execute(QUERY_3)
        # self.response.write(' GuestID, Room Number,	      Arrival Date,	          Departure Date  Room Phone Number\n')

        # QUERY_4 ="SELECT DISTINCT E.FirstName, E.LastName, E.EmployeeID FROM VALET_ATTENDANT E JOIN VALET_LOG L ON L.EmployeeID = E.EmployeeID JOIN VEHICLE V ON V.TicketNumber = L.TicketNumber WHERE V.LicensePlate = 'EFG4567'"
        # cursor.execute(QUERY_4)
        # self.response.write('FirstName, LastName, EmployeeID\n')

        # QUERY_5 = "SELECT G.FirstName, G.LastName FROM GUEST G JOIN TICKET T ON T.GuestID = G.GuestID JOIN VEHICLE V ON V.TicketNumber = T.TicketNumber WHERE V.Manufacturer = 'Toyota' and V.Model = 'Camary' and V.Color = 'Grey' and V.Year = 2005"
        # cursor.execute(QUERY_5)
        # self.response.write('First Name, Last Name\n')

        # QUERY_6 = "SELECT G.GuestID, G.FirstName, G.LastName FROM GUEST G JOIN STAY S ON G.GuestID = S.GuestID WHERE RoomPhoneNumber = 7575091023"
        # cursor.execute(QUERY_6)
        # self.response.write('GuestID, First name, Last name\n')

        # QUERY_7 = "SELECT EmployeeID,HOUR(TIMEDIFF(Endtime, StartTime))*7.25 AS 'WAGE' FROM SHIFT WHERE EmployeeID = '01A3X5'"
        # cursor.execute(QUERY_7)
        # self.response.write('Employee ID,	Wage\n')

        # QUERY_8 = "Select CONCAT(FirstName,' ',LastName) as 'Full Name' FROM VALET_ATTENDANT WHERE Transmission_Comfort LIKE '%MANUAL%'"
        # cursor.execute(QUERY_8)
        # self.response.write('Full Name\n')

        # QUERY_9 = "SELECT ParkingLevel  FROM VEHICLE WHERE LicensePlate = 'GOTHAM'"
        # cursor.execute(QUERY_9)
        # self.response.write('Parking Level\n')

        # QUERY_10 = "SELECT D.Information FROM DAMAGE D JOIN VEHICLE V ON D.TicketNumber = V.TicketNumber WHERE V.Manufacturer = 'Tesla' and V.Model = 'Model 3' and V.Year = 2018 and V.LicensePlate = 'DBS508'"
        # cursor.execute(QUERY_10)
        # self.response.write('DAMAGE INFORMATION\n')

        # QUERY_11 = "SELECT S.ArrivalDate FROM STAY S JOIN GUEST G ON G.GuestID = S.GuestID JOIN TICKET T ON T.GuestID = G.GuestID JOIN VEHICLE V ON V.TicketNumber = T.TicketNumber WHERE V.Manufacturer = 'Tesla' and V.Model = 'Model 3' and V.Color = 'Grey' and V.Year =2018"
        # cursor.execute(QUERY_11)
        # self.response.write('		Arrival Date\n')

        # QUERY_12 = "SELECT E.EmployeeID, CONCAT(E.FirstName,' ',E.LastName) as 'Full Name' FROM VALET_ATTENDANT E JOIN SHIFT S ON S.EmployeeID = E.EmployeeID WHERE S.ShiftID = 12345"
        # cursor.execute(QUERY_12)
        # self.response.write('Employee ID, Full Name\n')

        # QUERY_13 = "SELECT FirstName, LastName FROM VEHICLE V JOIN VALET_LOG L ON L.TicketNumber = V.TicketNumber JOIN VALET_ATTENDANT A ON A.EmployeeID = L.EmployeeID WHERE V.Model = 'Camary'"
        # cursor.execute(QUERY_13)
        # self.response.write('First Name, Last Name\n')

        # QUERY_14 = "SELECT V.Manufacturer, V.Model, V.Color, V.LicensePlate FROM VEHICLE V JOIN TICKET T ON T.TicketNumber = V.TicketNumber JOIN GUEST G ON G.GuestID = T.GuestID WHERE G.FirstName = 'Mary' and G.LastName = 'Jane'"
        # cursor.execute(QUERY_14)
        # self.response.write('Manufacturer, Model, Color, License Plate\n')

        # QUERY_15 = "SELECT  CONCAT(E.FirstName,' ',E.LastName) as 'Full Name'  FROM VALET_ATTENDANT E JOIN DAMAGE R ON R.EmployeeID = E.EmployeeID WHERE R.ReportID = '101123'"
        # cursor.execute(QUERY_15)
        # self.response.write('Full Name\n')

        # QUERY_16 = "SELECT S.GuestID,DATEDIFF(S.DepartureDate, S.ArrivalDate)*24 AS 'CHARGE' FROM STAY S JOIN GUEST G ON G.GuestID = S.GuestID WHERE G.FirstName = 'Steven' AND G.LastName = 'Jermstad'"
        # cursor.execute(QUERY_16)
        # self.response.write('Guest ID, Charge\n')

        # QUERY_17 = "SELECT GuestID FROM STAY WHERE DepartureDate = '2018-10-20'"
        # cursor.execute(QUERY_17)
        # self.response.write('GuestID\n')

        QUERY_18 = "SELECT COUNT(CarType) AS 'Number of Sedans'FROM VEHICLE WHERE CarType = 'Sedan'"
        cursor.execute(QUERY_18)
        self.response.write('Number of Cars\n')

        # QUERY_19 = "SELECT COUNT(Fuel) AS 'Number of electric cars' FROM VEHICLE WHERE Fuel = 'Electric'"
        # cursor.execute(QUERY_19)
        # self.response.write('Number of Cars\n')

        # QUERY 20
        # cursor.execute('INSERT INTO INSERT_GUEST VALUES(%s, %s, %s)',(956241, 'Andy', 'Griffin'))
        # cursor.execute('SELECT * FROM GUEST')
        # db.commit()
        # self.response.write('GuestID, First Name, Last Name\n')

        # QUERY_21 = "UPDATE STAY SET DepartureDate = CURDATE() WHERE GuestID = 'DBS508'"
        # cursor.execute(QUERY_21)
        # cursor.execute('SELECT * FROM STAY')
        # self.response.write('RNumber,GuestID, 	      Arrival Date, 	          Departure Date, Room Phone Number\n')

        # QUERY_22 = "DELETE FROM GUEST WHERE GuestID = '956241'"
        # cursor.execute(QUERY_22)
        # cursor.execute('SELECT * FROM GUEST')
        # db.commit()
        # self.response.write('GuestID,   First Name, Last Name	\n')

        for r in cursor.fetchall():
            self.response.write('{}\n'.format(r))


app = webapp2.WSGIApplication([('/', MainPage), ], debug=True)

# [END all]