from django.db import models


class AircraftType(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'aircraft_type'


class CarrierFlights(models.Model):
    id_carrier = models.IntegerField(null=True)
    numb_flight = models.IntegerField(null=True)
    date_f = models.DateField(null=True)
    id_aircraft_type = models.IntegerField(null=True)
    free_seats = models.IntegerField(null=True)

    @property
    def fullname(self):
        return self.numb_flight

    class Meta:
        db_table = 'carrier_flights'


class Carriers(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'carriers'


class City(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'city'


class ClientOrders(models.Model):
    client_model = models.ForeignKey('Clients', models.DO_NOTHING, null=False, db_column='id_client')
    date_order = models.DateField(null=True)
    id_order_type = models.IntegerField(null=True)

    @property
    def client(self):
        return self.client_model.id

    def date(self):
        return self.date_order

    def ordertype(self):
        return self.id_order_type

    class Meta:
        db_table = 'client_orders'


class ClientTours(models.Model):
    id_routes = models.IntegerField(null=True)
    id_client_orders = models.IntegerField(null=True)
    id_carrier_flights = models.IntegerField(null=True)
    seat = models.CharField(max_length=20)

    @property
    def route(self):
        return self.id_routes

    def client_order(self):
        return self.id_client_orders

    def carrier_flight(self):
        return self.id_carrier_flights

    def sseat(self):
        return self.seat

    class Meta:
        db_table = 'client_tours'


class Clients(models.Model):
    s_name = models.CharField(max_length=512)
    f_name = models.CharField(max_length=512)
    t_name = models.CharField(max_length=512)
    phone = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.s_name

    class Meta:
        db_table = 'clients'


class Country(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'country'


class EmployeeMotions(models.Model):
    id_employee = models.IntegerField(null=True)
    id_position = models.IntegerField(null=True)
    id_reason = models.IntegerField(null=True)
    order = models.CharField(max_length=512)
    date_order = models.DateField(null=True)

    @property
    def idemployee(self):
        return self.id_employee

    def idposition(self):
        return self.id_position

    def oorder(self):
        return self.order

    class Meta:
        db_table = 'employee_motions'


class Employees(models.Model):
    s_name = models.CharField(max_length=512)
    f_name = models.CharField(max_length=512)
    t_name = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=512)
    hb_day = models.DateField(null=True)
    id_position = models.IntegerField(null=True)
    salary = models.FloatField(null=True)

    @property
    def ss_name(self):
        return self.s_name

    def ff_name(self):
        return self.f_name

    def tt_name(self):
        return self.t_name

    class Meta:
        db_table = 'employees'


class Hotel(models.Model):
    name = models.CharField(max_length=512)
    id_hotel_type = models.IntegerField(null=True)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'hotel'


class HotelType(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'hotel_type'


class OrderType(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'order_type'


class Position(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'position'


class ReasonForTransfer(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'reason_for_transfer'


class Routes(models.Model):
    name = models.CharField(max_length=512)
    id_country = models.IntegerField(null=True)
    id_city = models.IntegerField(null=True)
    id_hotel = models.IntegerField(null=True)
    id_carrier = models.IntegerField(null=True)
    id_employee = models.IntegerField(null=True)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'routes'


class SeatType(models.Model):
    name = models.CharField(max_length=512)

    @property
    def fullname(self):
        return self.name

    class Meta:
        db_table = 'seat_type'
